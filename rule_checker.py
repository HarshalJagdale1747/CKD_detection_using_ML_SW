def rule_based_check(vals):
    sc, bu, al, sg, sod, pot, hemo, htn, dm, ane = vals

    count = 0
    
    if sc > 1.3: count += 1
    if bu > 50: count += 1
    if al > 1: count += 1
    if sg < 1.015: count += 1
    if pot > 5.0: count += 1
    if sod < 135: count += 1
    if hemo < 12: count += 1
    if htn == 1: count += 1
    if dm == 1: count += 1
    if ane == 1: count += 1

    if count >= 4:
        return "High Risk"
    return "Normal"
