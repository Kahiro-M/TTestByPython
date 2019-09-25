import numpy as np
from scipy import stats

service = np.array([1,0,0,0,1,0,1,0,0,0])
cv = np.array([0,1,1,0,1,1,1,1,0,1])
print('対応があるt検定')
print(stats.ttest_rel(service, cv))
print('対応がないt検定')
print(stats.ttest_ind(service, cv, equal_var = False))


# stats.ttest_ind(service, cv)

# # serviceの不偏分散
# service_var = np.var(service,ddof=1)
# # cvの不偏分散
# cv_var = np.var(cv,ddof=1)

# # serviceの自由度
# service_df = len(service) - 1

# # cvの自由度
# cv_df = len(cv) - 1

# # F比の値
# f = service_var / cv_var

# one_sided_pval1 = stats.f.cdf(f, service_df, cv_df)  # 片側検定のp値 1
# one_sided_pval2 = stats.f.sf(f, service_df, cv_df)   # 片側検定のp値 2
# two_sided_pval = min(one_sided_pval1, one_sided_pval2) * 2  # 両側検定のp値
# print('ウェルチのt検定')
# print('F:       ', round(f, 3))
# print('p-value: ', round(two_sided_pval, 5))

