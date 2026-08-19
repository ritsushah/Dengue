###############################################################################
#
# Diagnostic Test Accuracy Meta-Analysis: FIA vs ELISA for Dengue NS1
#
# Bivariate Random-Effects Model (Reitsma) / HSROC Analysis
#
# Methods:
#   - Reitsma et al. (2005) J Clin Epidemiol 58:982-990
#   - Rutter & Gatsonis (2001) Stat Med 20:2865-2884
#   - Harbord et al. (2007) Biostatistics 8:239-251
#   - Deeks et al. (2005) J Clin Epidemiol 58:882-893
#
# Software: R >= 4.3.0 with mada >= 0.5.12, metafor, meta, robvis
#
###############################################################################

# ============================================================================
# 0. ENVIRONMENT SETUP
# ============================================================================

required_packages <- c("mada", "metafor", "meta", "mvmeta",
                       "robvis", "ggplot2", "gridExtra", "dplyr",
                       "tidyr", "readr", "openxlsx", "boot")

for (pkg in required_packages) {
  if (!requireNamespace(pkg, quietly = TRUE)) {
    install.packages(pkg, repos = "https://cloud.r-project.org")
  }
}

library(mada)
library(metafor)
library(meta)
library(robvis)
library(ggplot2)
library(gridExtra)
library(dplyr)

cat("All packages loaded successfully.\n")
cat("mada version:", as.character(packageVersion("mada")), "\n")
cat("metafor version:", as.character(packageVersion("metafor")), "\n")
cat("R version:", R.version.string, "\n")

# ============================================================================
# 1. DATA INPUT
# ============================================================================
# Replace the placeholder data below with your actual extracted 2x2 table data.
# Each row = one study. Required columns: TP, FP, FN, TN.
#
# Data source: extraction_template.md Summary Table
# ============================================================================

fia_data <- data.frame(
  study_id       = c("Pohekar_2023", "Ghogre_2021", "Chaiyo_2022",
                     "Study_D", "Study_E", "Study_F",
                     "Study_G", "Study_H", "Study_I", "Study_J"),
  first_author   = c("Pohekar", "Ghogre", "Chaiyo",
                     "Author_D", "Author_E", "Author_F",
                     "Author_G", "Author_H", "Author_I", "Author_J"),
  year           = c(2023, 2021, 2022, 2022, 2021, 2023,
                     2020, 2024, 2023, 2022),
  country        = c("India", "India", "Thailand",
                     "Brazil", "Malaysia", "India",
                     "Philippines", "Vietnam", "Colombia", "Indonesia"),
  fia_brand      = c("STANDARD F", "QUANTI CARD", "STANDARD F",
                     "STANDARD F", "STANDARD F", "QUANTI CARD",
                     "STANDARD F", "STANDARD F", "STANDARD F", "STANDARD F"),
  ref_standard   = c("ELISA", "ELISA", "RT-PCR+ELISA",
                     "RT-PCR", "RT-PCR", "ELISA",
                     "RT-PCR", "Composite", "RT-PCR", "RT-PCR"),
  fever_category = c("mixed", "early", "mixed",
                     "early", "late", "early",
                     "mixed", "early", "late", "mixed"),
  infection_type = c("mixed", "primary", "mixed",
                     "secondary", "primary", "primary",
                     "mixed", "secondary", "mixed", "mixed"),

  # ---- 2x2 table values (FIA vs Reference Standard) ----
  # >>> REPLACE THESE WITH ACTUAL EXTRACTED DATA <<<
  TP = c(195, 55, 125, 89, 72, 48, 110, 65, 58, 94),
  FP = c(8,   2,  12,  3,  5,  3,   7,  4,  6,  5),
  FN = c(5,   2,  33,  7, 11,  4,  15,  8, 12,  9),
  TN = c(92,  26, 234, 51, 62, 30,  68, 73, 74, 42),

  stringsAsFactors = FALSE
)

# Optional: ELISA data for head-to-head comparison
# Only include studies where both FIA and ELISA were tested on the same specimens
elisa_data <- data.frame(
  study_id     = c("Pohekar_2023", "Ghogre_2021", "Chaiyo_2022",
                   "Study_D", "Study_F"),
  first_author = c("Pohekar", "Ghogre", "Chaiyo", "Author_D", "Author_F"),
  year         = c(2023, 2021, 2022, 2022, 2023),

  # ---- 2x2 table values (ELISA vs Reference Standard) ----
  # >>> REPLACE THESE WITH ACTUAL EXTRACTED DATA <<<
  TP = c(192, 56, 130, 90, 50),
  FP = c(5,   1,   8,  2,  2),
  FN = c(8,   1,  28,  6,  2),
  TN = c(95,  27, 238, 52, 31),

  stringsAsFactors = FALSE
)

cat("\n--- FIA Data Summary ---\n")
cat("Number of studies:", nrow(fia_data), "\n")
cat("Total participants:", sum(fia_data$TP + fia_data$FP + fia_data$FN + fia_data$TN), "\n")
cat("Total dengue-positive:", sum(fia_data$TP + fia_data$FN), "\n")
cat("Total dengue-negative:", sum(fia_data$FP + fia_data$TN), "\n")

# ============================================================================
# 2. ZERO-CELL CORRECTION CHECK
# ============================================================================

check_zero_cells <- function(data) {
  zero_studies <- data %>%
    filter(TP == 0 | FP == 0 | FN == 0 | TN == 0)

  if (nrow(zero_studies) > 0) {
    cat("\nWARNING: Zero cells detected in", nrow(zero_studies), "studies:\n")
    print(zero_studies[, c("study_id", "TP", "FP", "FN", "TN")])
    cat("Continuity correction of 0.5 will be applied by mada::reitsma().\n")
  } else {
    cat("\nNo zero cells detected. No continuity correction needed.\n")
  }
}

check_zero_cells(fia_data)

# ============================================================================
# 3. DESCRIPTIVE STATISTICS & INDIVIDUAL STUDY ESTIMATES
# ============================================================================

cat("\n", paste(rep("=", 70), collapse = ""), "\n")
cat("SECTION 3: DESCRIPTIVE STATISTICS\n")
cat(paste(rep("=", 70), collapse = ""), "\n\n")

fia_desc <- madad(fia_data, correction = 0.5, level = 0.95)
print(fia_desc)

sens_i <- fia_data$TP / (fia_data$TP + fia_data$FN)
spec_i <- fia_data$TN / (fia_data$TN + fia_data$FP)
ppv_i  <- fia_data$TP / (fia_data$TP + fia_data$FP)
npv_i  <- fia_data$TN / (fia_data$TN + fia_data$FN)
dor_i  <- (fia_data$TP * fia_data$TN) / (fia_data$FP * fia_data$FN)
plr_i  <- sens_i / (1 - spec_i)
nlr_i  <- (1 - sens_i) / spec_i

study_estimates <- data.frame(
  Study       = fia_data$study_id,
  N           = fia_data$TP + fia_data$FP + fia_data$FN + fia_data$TN,
  Prevalence  = round((fia_data$TP + fia_data$FN) /
                  (fia_data$TP + fia_data$FP + fia_data$FN + fia_data$TN), 3),
  Sensitivity = round(sens_i, 3),
  Specificity = round(spec_i, 3),
  PPV         = round(ppv_i, 3),
  NPV         = round(npv_i, 3),
  PLR         = round(plr_i, 2),
  NLR         = round(nlr_i, 3),
  DOR         = round(dor_i, 1)
)

cat("\nIndividual Study Estimates:\n")
print(study_estimates, row.names = FALSE)

# ============================================================================
# 4. PRIMARY ANALYSIS: BIVARIATE REITSMA MODEL
# ============================================================================

cat("\n", paste(rep("=", 70), collapse = ""), "\n")
cat("SECTION 4: BIVARIATE REITSMA MODEL (PRIMARY ANALYSIS)\n")
cat(paste(rep("=", 70), collapse = ""), "\n\n")

fit_reitsma <- reitsma(fia_data,
                       correction = 0.5,
                       correction.control = "all",
                       method = "reml")

cat("--- Model Summary ---\n")
summary_fit <- summary(fit_reitsma)
print(summary_fit)

pooled_sens <- plogis(coef(fit_reitsma)[1])
pooled_fpr  <- plogis(coef(fit_reitsma)[2])
pooled_spec <- 1 - pooled_fpr

cat("\n--- Pooled Estimates ---\n")
cat(sprintf("Pooled Sensitivity: %.3f (%.1f%%)\n", pooled_sens, pooled_sens * 100))
cat(sprintf("Pooled Specificity: %.3f (%.1f%%)\n", pooled_spec, pooled_spec * 100))
cat(sprintf("Pooled FPR:         %.3f (%.1f%%)\n", pooled_fpr, pooled_fpr * 100))

pooled_plr <- pooled_sens / pooled_fpr
pooled_nlr <- (1 - pooled_sens) / pooled_spec
pooled_dor <- (pooled_sens / (1 - pooled_sens)) / (pooled_fpr / (1 - pooled_fpr))

cat(sprintf("Pooled PLR:         %.2f\n", pooled_plr))
cat(sprintf("Pooled NLR:         %.3f\n", pooled_nlr))
cat(sprintf("Pooled DOR:         %.1f\n", pooled_dor))

# HSROC parameters (extracted from reitsma summary which provides both)
cat("\n--- HSROC Parameters ---\n")
cat("(Extracted from bivariate model — equivalent parameterization)\n")
cat("See summary output above for Lambda (accuracy), Theta (threshold),\n")
cat("beta (symmetry) parameters.\n")

# ============================================================================
# 5. CONFIDENCE INTERVALS VIA PARAMETRIC BOOTSTRAP
# ============================================================================

cat("\n", paste(rep("=", 70), collapse = ""), "\n")
cat("SECTION 5: 95% CONFIDENCE INTERVALS FOR DERIVED MEASURES\n")
cat(paste(rep("=", 70), collapse = ""), "\n\n")

vcov_fit <- vcov(fit_reitsma)
coefs    <- coef(fit_reitsma)

set.seed(42)
n_boot <- 10000
boot_samples <- MASS::mvrnorm(n_boot, mu = coefs, Sigma = vcov_fit)

boot_sens <- plogis(boot_samples[, 1])
boot_fpr  <- plogis(boot_samples[, 2])
boot_spec <- 1 - boot_fpr
boot_plr  <- boot_sens / boot_fpr
boot_nlr  <- (1 - boot_sens) / boot_spec
boot_dor  <- (boot_sens / (1 - boot_sens)) / (boot_fpr / (1 - boot_fpr))

ci_table <- data.frame(
  Measure     = c("Sensitivity", "Specificity", "PLR", "NLR", "DOR"),
  Estimate    = c(pooled_sens, pooled_spec, pooled_plr, pooled_nlr, pooled_dor),
  CI_lower    = c(quantile(boot_sens, 0.025),
                  quantile(boot_spec, 0.025),
                  quantile(boot_plr,  0.025),
                  quantile(boot_nlr,  0.025),
                  quantile(boot_dor,  0.025)),
  CI_upper    = c(quantile(boot_sens, 0.975),
                  quantile(boot_spec, 0.975),
                  quantile(boot_plr,  0.975),
                  quantile(boot_nlr,  0.975),
                  quantile(boot_dor,  0.975))
)

ci_table$Estimate <- round(ci_table$Estimate, 3)
ci_table$CI_lower <- round(ci_table$CI_lower, 3)
ci_table$CI_upper <- round(ci_table$CI_upper, 3)

cat("Pooled Estimates with 95% CIs (parametric bootstrap, n=10000):\n")
print(ci_table, row.names = FALSE)

# ============================================================================
# 6. FOREST PLOTS (COUPLED SENSITIVITY & SPECIFICITY)
# ============================================================================

cat("\n", paste(rep("=", 70), collapse = ""), "\n")
cat("SECTION 6: FOREST PLOTS\n")
cat(paste(rep("=", 70), collapse = ""), "\n\n")

dir.create("output/figures", recursive = TRUE, showWarnings = FALSE)

pdf("output/figures/forest_plot_fia.pdf", width = 12, height = 8)
forest(fia_desc,
       type = "sens",
       main = "FIA for Dengue NS1: Coupled Forest Plot")
dev.off()
cat("Forest plot saved: output/figures/forest_plot_fia.pdf\n")

# Custom ggplot2 forest plot with study labels
make_forest_ggplot <- function(data, measure_col, measure_name, color) {
  n_pos <- data$TP + data$FN
  n_neg <- data$FP + data$TN

  if (measure_name == "Sensitivity") {
    est   <- data$TP / n_pos
    se    <- sqrt(est * (1 - est) / n_pos)
  } else {
    est   <- data$TN / n_neg
    se    <- sqrt(est * (1 - est) / n_neg)
  }

  ci_lo <- pmax(est - 1.96 * se, 0)
  ci_hi <- pmin(est + 1.96 * se, 1)

  df <- data.frame(
    study = data$study_id,
    est   = est,
    lo    = ci_lo,
    hi    = ci_hi,
    stringsAsFactors = FALSE
  )
  df$study <- factor(df$study, levels = rev(df$study))

  ggplot(df, aes(x = est, y = study)) +
    geom_point(size = 3, color = color) +
    geom_errorbarh(aes(xmin = lo, xmax = hi), height = 0.2, color = color) +
    geom_vline(xintercept = mean(est), linetype = "dashed", color = "grey40") +
    scale_x_continuous(limits = c(0, 1), breaks = seq(0, 1, 0.2),
                       labels = scales::percent_format(accuracy = 1)) +
    labs(x = measure_name, y = NULL,
         title = paste(measure_name, "— FIA for Dengue NS1")) +
    theme_minimal(base_size = 12) +
    theme(panel.grid.minor = element_blank(),
          plot.title = element_text(face = "bold", size = 13))
}

p_sens <- make_forest_ggplot(fia_data, "TP", "Sensitivity", "#2166AC")
p_spec <- make_forest_ggplot(fia_data, "TN", "Specificity", "#B2182B")

pdf("output/figures/coupled_forest_fia.pdf", width = 14, height = 7)
gridExtra::grid.arrange(p_sens, p_spec, ncol = 2)
dev.off()
cat("Coupled forest plot saved: output/figures/coupled_forest_fia.pdf\n")

# ============================================================================
# 7. SROC CURVE
# ============================================================================

cat("\n", paste(rep("=", 70), collapse = ""), "\n")
cat("SECTION 7: SUMMARY ROC (SROC) CURVE\n")
cat(paste(rep("=", 70), collapse = ""), "\n\n")

pdf("output/figures/sroc_fia.pdf", width = 8, height = 8)
plot(fit_reitsma,
     sroclwd = 2,
     main = "HSROC Curve — FIA for Dengue NS1 Antigen",
     predict = TRUE,
     cex = 1.5,
     xlim = c(0, 0.5),
     ylim = c(0.5, 1))
legend("bottomright",
       legend = c("Summary point", "95% Confidence region",
                  "95% Prediction region", "Individual studies"),
       pch = c(1, NA, NA, 19),
       lty = c(NA, 1, 2, NA),
       col = c("black", "black", "black", "grey40"),
       bty = "n", cex = 0.9)
dev.off()
cat("SROC curve saved: output/figures/sroc_fia.pdf\n")

# ============================================================================
# 8. HETEROGENEITY ASSESSMENT
# ============================================================================

cat("\n", paste(rep("=", 70), collapse = ""), "\n")
cat("SECTION 8: HETEROGENEITY ASSESSMENT\n")
cat(paste(rep("=", 70), collapse = ""), "\n\n")

# 8a. Cochran's Q and I-squared for Sensitivity (univariate)
logit_sens  <- log(sens_i / (1 - sens_i))
var_sens    <- 1 / fia_data$TP + 1 / fia_data$FN
rma_sens    <- rma(yi = logit_sens, vi = var_sens, method = "REML")

cat("--- Heterogeneity in Sensitivity (logit scale) ---\n")
cat(sprintf("Cochran's Q: %.2f, df = %d, p = %.4f\n",
            rma_sens$QE, rma_sens$k - 1, rma_sens$QEp))
cat(sprintf("I-squared:   %.1f%%\n", rma_sens$I2))
cat(sprintf("tau-squared: %.4f\n", rma_sens$tau2))

# 8b. Cochran's Q and I-squared for Specificity (univariate)
logit_spec  <- log(spec_i / (1 - spec_i))
var_spec    <- 1 / fia_data$TN + 1 / fia_data$FP
rma_spec    <- rma(yi = logit_spec, vi = var_spec, method = "REML")

cat("\n--- Heterogeneity in Specificity (logit scale) ---\n")
cat(sprintf("Cochran's Q: %.2f, df = %d, p = %.4f\n",
            rma_spec$QE, rma_spec$k - 1, rma_spec$QEp))
cat(sprintf("I-squared:   %.1f%%\n", rma_spec$I2))
cat(sprintf("tau-squared: %.4f\n", rma_spec$tau2))

# 8c. Bivariate heterogeneity (variance-covariance from Reitsma model)
cat("\n--- Bivariate Heterogeneity (Reitsma Model) ---\n")
cat("Between-study variance-covariance matrix (Sigma):\n")
print(fit_reitsma$Psi)

cat(sprintf("\ntau^2 (logit-sensitivity): %.4f\n", fit_reitsma$Psi[1, 1]))
cat(sprintf("tau^2 (logit-FPR):         %.4f\n", fit_reitsma$Psi[2, 2]))

rho <- fit_reitsma$Psi[1, 2] /
       sqrt(fit_reitsma$Psi[1, 1] * fit_reitsma$Psi[2, 2])
cat(sprintf("Correlation (rho):         %.3f\n", rho))

if (rho < -0.3) {
  cat("Interpretation: Negative correlation suggests threshold effect present.\n")
} else if (rho > 0.3) {
  cat("Interpretation: Positive correlation — threshold effect unlikely.\n")
} else {
  cat("Interpretation: Weak correlation — no clear threshold effect.\n")
}

# 8d. I-squared interpretation
interpret_i2 <- function(i2) {
  if (i2 < 40)       return("might not be important (0-40%)")
  else if (i2 < 60)  return("moderate (30-60%)")
  else if (i2 < 90)  return("substantial (50-90%)")
  else                return("considerable (75-100%)")
}

cat(sprintf("\nI-squared interpretation (Sensitivity): %s\n",
            interpret_i2(rma_sens$I2)))
cat(sprintf("I-squared interpretation (Specificity): %s\n",
            interpret_i2(rma_spec$I2)))

# ============================================================================
# 9. PUBLICATION BIAS: DEEKS' FUNNEL PLOT ASYMMETRY TEST
# ============================================================================

cat("\n", paste(rep("=", 70), collapse = ""), "\n")
cat("SECTION 9: DEEKS' FUNNEL PLOT ASYMMETRY TEST\n")
cat(paste(rep("=", 70), collapse = ""), "\n\n")

# Deeks' method: regress log(DOR) on 1/sqrt(ESS) and test for asymmetry
# ESS = effective sample size = 4 * n_pos * n_neg / (n_pos + n_neg)
# Reference: Deeks JJ et al. (2005) J Clin Epidemiol 58:882-893

deeks_funnel_test <- function(data, plot_file = NULL) {

  tp <- data$TP; fp <- data$FP; fn <- data$FN; tn <- data$TN
  n_pos <- tp + fn
  n_neg <- fp + tn

  dor_adj <- ((tp + 0.5) * (tn + 0.5)) / ((fp + 0.5) * (fn + 0.5))
  log_dor <- log(dor_adj)

  ess <- 4 * n_pos * n_neg / (n_pos + n_neg)
  inv_sqrt_ess <- 1 / sqrt(ess)

  reg_model <- lm(log_dor ~ inv_sqrt_ess)
  reg_summary <- summary(reg_model)

  slope     <- coef(reg_model)[2]
  slope_se  <- reg_summary$coefficients[2, 2]
  p_value   <- reg_summary$coefficients[2, 4]

  cat("Deeks' Funnel Plot Asymmetry Test:\n")
  cat(sprintf("  Regression slope:    %.4f\n", slope))
  cat(sprintf("  Slope SE:            %.4f\n", slope_se))
  cat(sprintf("  t-statistic:         %.3f\n", slope / slope_se))
  cat(sprintf("  p-value:             %.4f\n", p_value))

  if (p_value < 0.10) {
    cat("  Result: SIGNIFICANT (p < 0.10) — potential publication bias detected.\n")
  } else {
    cat("  Result: Non-significant (p >= 0.10) — no evidence of publication bias.\n")
  }

  if (!is.null(plot_file)) {
    pdf(plot_file, width = 7, height = 7)
    plot(inv_sqrt_ess, log_dor,
         pch = 19, cex = 1.3, col = "steelblue",
         xlab = expression(1 / sqrt(ESS)),
         ylab = "ln(DOR)",
         main = "Deeks' Funnel Plot Asymmetry Test",
         sub = sprintf("Regression test: slope = %.3f, p = %.4f", slope, p_value))
    abline(reg_model, col = "red", lwd = 2)
    dev.off()
    cat(sprintf("  Funnel plot saved: %s\n", plot_file))
  }

  return(list(slope = slope, se = slope_se, p_value = p_value,
              model = reg_model))
}

deeks_result <- deeks_funnel_test(fia_data,
                                  plot_file = "output/figures/deeks_funnel.pdf")

# ============================================================================
# 10. SUBGROUP ANALYSES
# ============================================================================

cat("\n", paste(rep("=", 70), collapse = ""), "\n")
cat("SECTION 10: SUBGROUP ANALYSES\n")
cat(paste(rep("=", 70), collapse = ""), "\n\n")

run_subgroup_analysis <- function(data, group_var, group_name,
                                  min_studies = 4) {
  groups <- unique(data[[group_var]])
  groups <- groups[groups != "mixed"]

  cat(sprintf("\n--- Subgroup Analysis: %s ---\n", group_name))

  results <- list()
  for (g in groups) {
    sub <- data[data[[group_var]] == g, ]

    if (nrow(sub) < min_studies) {
      cat(sprintf("  %s: Only %d studies (minimum %d required). Skipped.\n",
                  g, nrow(sub), min_studies))
      next
    }

    cat(sprintf("\n  Subgroup: %s (k = %d studies)\n", g, nrow(sub)))

    tryCatch({
      fit_sub <- reitsma(sub, correction = 0.5, method = "reml")

      sub_sens <- plogis(coef(fit_sub)[1])
      sub_spec <- 1 - plogis(coef(fit_sub)[2])
      sub_fpr  <- plogis(coef(fit_sub)[2])
      sub_plr  <- sub_sens / sub_fpr
      sub_nlr  <- (1 - sub_sens) / sub_spec
      sub_dor  <- (sub_sens / (1 - sub_sens)) / (sub_fpr / (1 - sub_fpr))

      cat(sprintf("    Pooled Sensitivity: %.3f (%.1f%%)\n",
                  sub_sens, sub_sens * 100))
      cat(sprintf("    Pooled Specificity: %.3f (%.1f%%)\n",
                  sub_spec, sub_spec * 100))
      cat(sprintf("    PLR: %.2f  |  NLR: %.3f  |  DOR: %.1f\n",
                  sub_plr, sub_nlr, sub_dor))

      results[[g]] <- list(
        group = g, k = nrow(sub),
        sensitivity = sub_sens, specificity = sub_spec,
        plr = sub_plr, nlr = sub_nlr, dor = sub_dor,
        fit = fit_sub
      )
    }, error = function(e) {
      cat(sprintf("    ERROR fitting model: %s\n", e$message))
    })
  }

  return(results)
}

# 10a. Subgroup: Fever duration (early <=3 days vs late >3 days)
cat("=== 10a. Fever Duration ===\n")
subgroup_fever <- run_subgroup_analysis(
  fia_data, "fever_category", "Days of Fever (early ≤3 vs late >3)")

# 10b. Subgroup: Primary vs Secondary infection
cat("\n=== 10b. Infection Type ===\n")
subgroup_infection <- run_subgroup_analysis(
  fia_data, "infection_type", "Infection Type (Primary vs Secondary)")

# 10c. Subgroup: Reference standard type
cat("\n=== 10c. Reference Standard ===\n")
subgroup_refstd <- run_subgroup_analysis(
  fia_data, "ref_standard", "Reference Standard Type")

# ============================================================================
# 11. META-REGRESSION (BIVARIATE WITH COVARIATES)
# ============================================================================

cat("\n", paste(rep("=", 70), collapse = ""), "\n")
cat("SECTION 11: META-REGRESSION\n")
cat(paste(rep("=", 70), collapse = ""), "\n\n")

run_meta_regression <- function(data, covariate_col, covariate_name) {
  cat(sprintf("\n--- Meta-Regression: %s ---\n", covariate_name))

  data$covariate <- factor(data[[covariate_col]])

  if (length(levels(data$covariate)) < 2) {
    cat("  Insufficient covariate levels (< 2). Skipped.\n")
    return(NULL)
  }

  tryCatch({
    formula_mr <- as.formula("cbind(tsens, tfpr) ~ covariate")
    fit_mr <- reitsma(data, formula = formula_mr,
                      correction = 0.5, method = "reml")

    cat("  Model summary:\n")
    print(summary(fit_mr))

    # Likelihood ratio test vs null model
    fit_null <- reitsma(data, correction = 0.5, method = "ml")
    fit_mr_ml <- reitsma(data, formula = formula_mr,
                         correction = 0.5, method = "ml")

    lr_stat <- -2 * (logLik(fit_null) - logLik(fit_mr_ml))
    df_diff <- length(coef(fit_mr_ml)) - length(coef(fit_null))

    if (df_diff > 0) {
      lr_p <- pchisq(as.numeric(lr_stat), df = df_diff, lower.tail = FALSE)
      cat(sprintf("  Likelihood ratio test vs null: chi2 = %.3f, df = %d, p = %.4f\n",
                  as.numeric(lr_stat), df_diff, lr_p))
    }

    return(fit_mr)
  }, error = function(e) {
    cat(sprintf("  ERROR: %s\n", e$message))
    return(NULL)
  })
}

# 11a. Meta-regression: reference standard type
mr_refstd <- run_meta_regression(fia_data, "ref_standard",
                                  "Reference Standard Type")

# 11b. Meta-regression: FIA brand
mr_brand <- run_meta_regression(fia_data, "fia_brand", "FIA Brand")

# 11c. Meta-regression: fever category
mr_fever <- run_meta_regression(fia_data, "fever_category",
                                 "Fever Duration Category")

# 11d. Meta-regression: infection type
mr_infect <- run_meta_regression(fia_data, "infection_type",
                                  "Infection Type")

# ============================================================================
# 12. HEAD-TO-HEAD COMPARISON: FIA vs ELISA
# ============================================================================

cat("\n", paste(rep("=", 70), collapse = ""), "\n")
cat("SECTION 12: HEAD-TO-HEAD COMPARISON — FIA vs ELISA\n")
cat(paste(rep("=", 70), collapse = ""), "\n\n")

if (nrow(elisa_data) >= 4) {

  fit_elisa <- reitsma(elisa_data, correction = 0.5, method = "reml")

  elisa_sens <- plogis(coef(fit_elisa)[1])
  elisa_spec <- 1 - plogis(coef(fit_elisa)[2])
  elisa_fpr  <- plogis(coef(fit_elisa)[2])
  elisa_plr  <- elisa_sens / elisa_fpr
  elisa_nlr  <- (1 - elisa_sens) / elisa_spec
  elisa_dor  <- (elisa_sens / (1 - elisa_sens)) / (elisa_fpr / (1 - elisa_fpr))

  # Fit FIA on the same subset of studies for fair comparison
  fia_subset <- fia_data[fia_data$study_id %in% elisa_data$study_id, ]
  fit_fia_sub <- reitsma(fia_subset, correction = 0.5, method = "reml")

  fia_sub_sens <- plogis(coef(fit_fia_sub)[1])
  fia_sub_spec <- 1 - plogis(coef(fit_fia_sub)[2])

  comparison <- data.frame(
    Test         = c("FIA (subset)", "ELISA"),
    k_studies    = c(nrow(fia_subset), nrow(elisa_data)),
    Sensitivity  = round(c(fia_sub_sens, elisa_sens), 3),
    Specificity  = round(c(fia_sub_spec, elisa_spec), 3),
    PLR          = round(c(fia_sub_sens / (1 - fia_sub_spec),
                           elisa_plr), 2),
    NLR          = round(c((1 - fia_sub_sens) / fia_sub_spec,
                           elisa_nlr), 3),
    stringsAsFactors = FALSE
  )

  cat("Head-to-Head Comparison (same specimens):\n")
  print(comparison, row.names = FALSE)

  # Comparative SROC plot
  pdf("output/figures/sroc_fia_vs_elisa.pdf", width = 9, height = 8)
  plot(fit_fia_sub,
       sroclwd = 2, col = "blue",
       main = "Comparative SROC — FIA vs ELISA for Dengue NS1",
       predict = FALSE,
       xlim = c(0, 0.5), ylim = c(0.5, 1))

  lines(sroc(fit_elisa), lwd = 2, col = "red")
  points(1 - elisa_spec, elisa_sens, pch = 17, cex = 2, col = "red")
  points(1 - fia_sub_spec, fia_sub_sens, pch = 16, cex = 2, col = "blue")

  legend("bottomright",
         legend = c("FIA (SROC)", "FIA (summary point)",
                    "ELISA (SROC)", "ELISA (summary point)"),
         lty = c(1, NA, 1, NA),
         pch = c(NA, 16, NA, 17),
         col = c("blue", "blue", "red", "red"),
         lwd = 2, bty = "n", cex = 0.9)
  dev.off()
  cat("Comparative SROC saved: output/figures/sroc_fia_vs_elisa.pdf\n")

} else {
  cat("Fewer than 4 studies with paired FIA & ELISA data.\n")
  cat("Head-to-head bivariate comparison requires ≥4 studies. Skipped.\n")
}

# ============================================================================
# 13. SENSITIVITY ANALYSES
# ============================================================================

cat("\n", paste(rep("=", 70), collapse = ""), "\n")
cat("SECTION 13: SENSITIVITY ANALYSES\n")
cat(paste(rep("=", 70), collapse = ""), "\n\n")

# 13a. Leave-one-out influence analysis
cat("--- 13a. Leave-One-Out Influence Analysis ---\n")

loo_results <- data.frame(
  excluded_study = character(),
  sens           = numeric(),
  spec           = numeric(),
  dor            = numeric(),
  stringsAsFactors = FALSE
)

for (i in seq_len(nrow(fia_data))) {
  fia_loo <- fia_data[-i, ]

  tryCatch({
    fit_loo  <- reitsma(fia_loo, correction = 0.5, method = "reml")
    loo_sens <- plogis(coef(fit_loo)[1])
    loo_fpr  <- plogis(coef(fit_loo)[2])
    loo_spec <- 1 - loo_fpr
    loo_dor  <- (loo_sens / (1 - loo_sens)) / (loo_fpr / (1 - loo_fpr))

    loo_results <- rbind(loo_results, data.frame(
      excluded_study = fia_data$study_id[i],
      sens           = round(loo_sens, 3),
      spec           = round(loo_spec, 3),
      dor            = round(loo_dor, 1)
    ))
  }, error = function(e) {
    cat(sprintf("  Error excluding %s: %s\n", fia_data$study_id[i], e$message))
  })
}

cat("\nLeave-One-Out Results:\n")
print(loo_results, row.names = FALSE)
cat(sprintf("\nOriginal pooled: Sens = %.3f, Spec = %.3f, DOR = %.1f\n",
            pooled_sens, pooled_spec, pooled_dor))
cat(sprintf("Range (Sens): %.3f - %.3f\n",
            min(loo_results$sens), max(loo_results$sens)))
cat(sprintf("Range (Spec): %.3f - %.3f\n",
            min(loo_results$spec), max(loo_results$spec)))

# 13b. ML vs REML comparison
cat("\n--- 13b. ML vs REML Comparison ---\n")

fit_ml <- reitsma(fia_data, correction = 0.5, method = "ml")
ml_sens <- plogis(coef(fit_ml)[1])
ml_spec <- 1 - plogis(coef(fit_ml)[2])

cat(sprintf("REML: Sens = %.3f, Spec = %.3f\n", pooled_sens, pooled_spec))
cat(sprintf("ML:   Sens = %.3f, Spec = %.3f\n", ml_sens, ml_spec))
cat(sprintf("Difference (Sens): %.4f\n", abs(pooled_sens - ml_sens)))
cat(sprintf("Difference (Spec): %.4f\n", abs(pooled_spec - ml_spec)))

# 13c. Alternative continuity corrections
cat("\n--- 13c. Continuity Correction Sensitivity ---\n")

for (cc in c(0.1, 0.5, 1.0)) {
  tryCatch({
    fit_cc  <- reitsma(fia_data, correction = cc, method = "reml")
    cc_sens <- plogis(coef(fit_cc)[1])
    cc_spec <- 1 - plogis(coef(fit_cc)[2])
    cat(sprintf("  Correction = %.1f: Sens = %.3f, Spec = %.3f\n",
                cc, cc_sens, cc_spec))
  }, error = function(e) {
    cat(sprintf("  Correction = %.1f: ERROR - %s\n", cc, e$message))
  })
}

# ============================================================================
# 14. QUADAS-2 VISUALIZATION
# ============================================================================

cat("\n", paste(rep("=", 70), collapse = ""), "\n")
cat("SECTION 14: QUADAS-2 RISK OF BIAS VISUALIZATION\n")
cat(paste(rep("=", 70), collapse = ""), "\n\n")

# QUADAS-2 data input for robvis
# Column order: Study, D1 (Patient Selection), D2 (Index Test),
#               D3 (Reference Standard), D4 (Flow & Timing), Overall, Weight
# Values: "Low", "High", or "Unclear"
#
# >>> REPLACE WITH ACTUAL QUADAS-2 ASSESSMENT DATA <<<

quadas_data <- data.frame(
  Study   = fia_data$study_id,
  D1      = c("Low", "Low", "Low", "Unclear", "Low",
              "Low", "High", "Low", "Low", "Unclear"),
  D2      = c("Low", "Low", "Low", "Low", "Low",
              "Unclear", "Low", "Low", "Low", "Low"),
  D3      = c("Unclear", "Unclear", "Low", "Low", "Low",
              "Unclear", "Low", "Low", "Low", "Low"),
  D4      = c("Low", "Low", "Low", "Low", "Low",
              "Low", "Unclear", "Low", "High", "Low"),
  Overall = c("Low", "Low", "Low", "Unclear", "Low",
              "Unclear", "High", "Low", "High", "Unclear"),
  Weight  = rep(1 / nrow(fia_data), nrow(fia_data)),
  stringsAsFactors = FALSE
)

# Traffic light plot
p_traffic <- rob_traffic_light(quadas_data, tool = "QUADAS-2",
                                colour = "cochrane", psize = 14)
ggsave("output/figures/quadas2_traffic_light.pdf", p_traffic,
       width = 10, height = 6)
cat("QUADAS-2 traffic light plot saved: output/figures/quadas2_traffic_light.pdf\n")

# Summary barplot
p_summary <- rob_summary(quadas_data, tool = "QUADAS-2",
                          overall = TRUE, weighted = TRUE,
                          colour = "cochrane")
ggsave("output/figures/quadas2_summary.pdf", p_summary,
       width = 8, height = 4)
cat("QUADAS-2 summary plot saved: output/figures/quadas2_summary.pdf\n")

# ============================================================================
# 15. EXPORT RESULTS
# ============================================================================

cat("\n", paste(rep("=", 70), collapse = ""), "\n")
cat("SECTION 15: EXPORT RESULTS\n")
cat(paste(rep("=", 70), collapse = ""), "\n\n")

dir.create("output/tables", recursive = TRUE, showWarnings = FALSE)

write.csv(study_estimates, "output/tables/individual_study_estimates.csv",
          row.names = FALSE)
write.csv(ci_table, "output/tables/pooled_estimates_with_ci.csv",
          row.names = FALSE)
write.csv(loo_results, "output/tables/leave_one_out_results.csv",
          row.names = FALSE)

cat("Tables exported to output/tables/\n")

# ============================================================================
# 16. SESSION INFO
# ============================================================================

cat("\n", paste(rep("=", 70), collapse = ""), "\n")
cat("SESSION INFO\n")
cat(paste(rep("=", 70), collapse = ""), "\n\n")
sessionInfo()

cat("\n\n====== ANALYSIS COMPLETE ======\n")
cat("All figures saved to: output/figures/\n")
cat("All tables saved to:  output/tables/\n")
cat("\nKey output files:\n")
cat("  - output/figures/forest_plot_fia.pdf\n")
cat("  - output/figures/coupled_forest_fia.pdf\n")
cat("  - output/figures/sroc_fia.pdf\n")
cat("  - output/figures/sroc_fia_vs_elisa.pdf\n")
cat("  - output/figures/deeks_funnel.pdf\n")
cat("  - output/figures/quadas2_traffic_light.pdf\n")
cat("  - output/figures/quadas2_summary.pdf\n")
cat("  - output/tables/individual_study_estimates.csv\n")
cat("  - output/tables/pooled_estimates_with_ci.csv\n")
cat("  - output/tables/leave_one_out_results.csv\n")
