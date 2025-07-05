import georinex as gr

print("🔍 Loading file just to inspect observables...")

# This will load only enough to extract the header
obs = gr.load("AUCK00NZL_R_20251200000_01D_30S_MO.rnx")

# Print available satellites and data variables
print("✅ Available satellites:", list(obs.sv.values))
print("✅ Available observables:", list(obs.data_vars))
