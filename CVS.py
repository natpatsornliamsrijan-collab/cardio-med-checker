import difflib

# ---------------- DATA ----------------

# full cardiovascular drug list
drugs = [
    "apixaban", "dabigatran", "edoxaban", "heparin", "rivaroxaban", "warfarin",
    "aspirin", "clopidogrel", "dipyridamole", "prasugrel", "ticagrelor",
    "benazepril", "captopril", "enalapril", "fosinopril", "lisinopril",
    "moexipril", "perindopril", "quinapril", "ramipril", "trandolapril",
    "azilsartan", "candesartan", "eprosartan", "irbesartan", "losartan",
    "olmesartan", "telmisartan", "valsartan",
    "acebutolol", "atenolol", "betaxolol", "bisoprolol", "metoprolol",
    "nadolol", "propranolol", "sotalol", "carvedilol", "labetalol",
    "amlodipine", "diltiazem", "felodipine", "nifedipine", "nimodipine",
    "nisoldipine", "verapamil",
    "atorvastatin", "fluvastatin", "lovastatin", "pitavastatin",
    "pravastatin", "rosuvastatin", "simvastatin",
    "niacin", "ezetimibe", "ezetimibe/simvastatin",
    "cholestyramine", "colesevelam", "colestipol",
    "alirocumab", "evolocumab",
    "acetazolamide", "amiloride", "bumetanide", "chlorothiazide",
    "chlorthalidone", "furosemide", "hydrochlorothiazide",
    "indapamide", "metolazone", "spironolactone", "torsemide",
    "isosorbide dinitrate", "isosorbide mononitrate",
    "hydralazine", "nitroglycerin", "minoxidil"
]

# supplements / foods
supplements = [
    "vitamin k", "vitamin d", "vitamin e",
    "omega-3", "garlic", "ginkgo",
    "american ginseng", "echinacea",
    "coenzyme q10", "grapefruit", "alcohol",
    "turmeric", "mint", "pomegranate", "red clover",
    "potassium", "peppermint", "fennel"
]

# synonyms
synonyms = {
    "fish oil": "omega-3",
    "vit d": "vitamin d",
    "vit k": "vitamin k",
    "vit e": "vitamin e",
    "coq10": "coenzyme q10",
    "ginseng": "american ginseng"
}

# specific interactions
interactions = [
    {"drug": "warfarin", "item": "vitamin k", "severity": "major"},
    {"drug": "warfarin", "item": "ginkgo", "severity": "major"},
    {"drug": "warfarin", "item": "garlic", "severity": "moderate"},
    {"drug": "warfarin", "item": "grapefruit", "severity": "minor"},
    {"drug": "warfarin", "item": "alcohol", "severity": "major"},
    {"drug": "aspirin", "item": "ginkgo", "severity": "major"},
    {"drug": "lisinopril", "item": "potassium", "severity": "major"},
    {"drug": "simvastatin", "item": "grapefruit", "severity": "major"},
    {"drug": "atorvastatin", "item": "grapefruit", "severity": "major"}
]

# -------- WARFARIN EXTENDED DATA --------
warfarin_extended = [
    {"item": "cranberry", "effect": "increase", "severity": "major"},
    {"item": "ginkgo", "effect": "increase", "severity": "major"},
    {"item": "ginger", "effect": "increase", "severity": "moderate"},
    {"item": "spinach", "effect": "decrease", "severity": "moderate"},
    {"item": "green tea", "effect": "decrease", "severity": "moderate"},
    {"item": "st john's wort", "effect": "decrease", "severity": "major"},
    {"item": "grapefruit", "effect": "uncertain", "severity": "major"},
    {"item": "garlic", "effect": "uncertain", "severity": "minor"},
    {"item": "vitamin e", "effect": "increase", "severity": "moderate"},
    {"item": "vitamin k", "effect": "decrease", "severity": "major"},
    {"item": "omega-3", "effect": "uncertain", "severity": "minor"},
    {"item": "alcohol", "effect": "increase", "severity": "moderate"}
]

# class interactions
drug_classes = {
    "statins": {
        "drugs": ["atorvastatin", "simvastatin"],
        "herbs": ["garlic", "turmeric", "mint", "pomegranate", "red clover"],
        "effect": "may increase drug levels and risk of muscle toxicity"
    },
    "beta blockers": {
        "drugs": ["propranolol", "metoprolol", "bisoprolol", "carvedilol"],
        "herbs": ["garlic", "turmeric", "red clover"],
        "effect": "may slow heart rate too much (bradycardia)"
    }
}

# evidence-based data
supplement_evidence = [
    {"supplement": "omega-3", "drug_group": "statins",
     "effect": "can help lower triglycerides", "evidence": "low"},
    {"supplement": "garlic", "drug_group": "warfarin",
     "effect": "no clear effect on INR", "evidence": "low"},
    {"supplement": "american ginseng", "drug_group": "warfarin",
     "effect": "may reduce drug levels", "evidence": "insufficient"},
    {"supplement": "echinacea", "drug_group": "warfarin",
     "effect": "may increase drug clearance", "evidence": "insufficient"}
]

# risk info
low_risk_drugs = ["pravastatin", "nadolol", "amiloride"]
high_risk_classes = {
    "statins": ["atorvastatin", "simvastatin"],
    "beta blockers": ["metoprolol", "propranolol"]
}

# ---------------- FUNCTIONS ----------------

def normalize_input(user_input, dataset):
    user_input = user_input.lower().strip()

    if user_input in synonyms:
        return synonyms[user_input]

    if user_input in dataset:
        return user_input

    suggestion = difflib.get_close_matches(user_input, dataset, n=1)
    if suggestion:
        answer = input(f"Do you mean '{suggestion[0]}'? (yes/no): ")
        if answer.lower() == "yes":
            return suggestion[0]

    print("Sorry, this item is not in our database yet.")
    print("Please consult a healthcare professional before using this combination.\n")
    return "unknown"


def explain_severity(severity):
    if severity == "major":
        return "This is a serious interaction. Avoid using them together."
    elif severity == "moderate":
        return "Use with caution. Monitoring or dose adjustment may be needed."
    elif severity == "minor":
        return "This interaction is usually mild but still worth noting."
    return ""


def check_interactions(user_drugs, item):
    return [i for i in interactions if i["drug"] in user_drugs and i["item"] == item]

def check_warfarin_extended(user_drugs, item):
    results = []
    if "warfarin" in user_drugs:
        for w in warfarin_extended:
            if w["item"] == item:
                results.append(w)
    return results


def explain_warfarin_effect(effect):
    if effect == "increase":
        return "May increase warfarin effect → higher bleeding risk"
    elif effect == "decrease":
        return "May reduce warfarin effect → risk of clot"
    elif effect == "uncertain":
        return "Effect is unclear or inconsistent in studies"
    return ""

def check_class(user_drugs, item):
    results = []
    for d in user_drugs:
        for cls, data in drug_classes.items():
            if d in data["drugs"] and item in data["herbs"]:
                results.append((cls, data["effect"]))
    return results


def check_evidence(user_drugs, item):
    results = []
    for d in user_drugs:
        for e in supplement_evidence:
            if item == e["supplement"] and e["drug_group"] in d:
                results.append(e)
    return results


def assess_risk(user_drugs):
    messages = []
    for d in user_drugs:
        if d in low_risk_drugs:
            messages.append(f"{d}: generally lower interaction risk")
        for cls, lst in high_risk_classes.items():
            if d in lst:
                messages.append(f"{d}: higher interaction risk ({cls})")
    return messages


# ---------------- MAIN ----------------

while True:

    user_drugs = []

    print("\nEnter your heart medications (lowercase):\n")

    while True:
        d = normalize_input(input("Drug name: "), drugs)
        if d:
            user_drugs.append(d)

        if input("Do you take another one? (yes/no): ").lower() != "yes":
            break

    item = normalize_input(input("\nEnter a supplement or food: "), supplements)
    if item == "unknown":
        print("\n--- Result ---\n")
        print("⚠️ This item is currently not available in our system.")
        print("We cannot confirm safety or interaction.")
        print("Please consult a doctor or pharmacist before use.\n")

    if input("Do you want to check another combination? (yes/no): ").lower() != "yes":
        print("Goodbye.")
        break
    else:
        continue

    print("\n--- Result ---\n")

    found = False

    # specific interactions
    for r in check_interactions(user_drugs, item):
        print(f"{r['drug']} + {r['item']}")
        print(f"Severity: {r['severity']}")
        print(explain_severity(r["severity"]))
        print()
        found = True

    # warfarin extended
    warfarin_results = check_warfarin_extended(user_drugs, item)

    for w in warfarin_results:
        print(f"Warfarin interaction with {item}")
        print(f"Effect: {w['effect']}")
        print(explain_warfarin_effect(w["effect"]))
        print(f"Severity: {w['severity']}")
        print(explain_severity(w["severity"]))
        print()
        found = True

    # class interactions
    for cls, eff in check_class(user_drugs, item):
        print(f"Drug class: {cls}")
        print(f"Possible effect: {eff}\n")
        found = True

    # evidence
    ev = check_evidence(user_drugs, item)
    if ev:
        print("Additional information:\n")
        for e in ev:
            print(f"{e['supplement']}: {e['effect']} (evidence: {e['evidence']})")
        print()
        found = True

    # risk
    risk = assess_risk(user_drugs)
    if risk:
        print("General risk notes:\n")
        for r in risk:
            print(r)
        print()

    if not found:
        print("No significant interaction found.\n")

    print("⚠️ Please consult a doctor or pharmacist before combining medications and supplements.\n")

    if input("Do you want to check another combination? (yes/no): ").lower() != "yes":
        print("Goodbye.")
        break
