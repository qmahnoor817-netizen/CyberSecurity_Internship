"""
Day 4 - Vishing & Smishing Awareness Script Generator
Produces TRAINING scripts (for security-awareness exercises), not
scripts to be used against real people outside an authorized program.
"""


def generate_vishing_script(target_company, attacker_role, pretext):
    return f"""
=== VISHING AWARENESS SCRIPT ===
Caller Role : {attacker_role}
Target Org  : {target_company}
Pretext     : {pretext}

[OPENER]
'Hi, this is Alex from {attacker_role} at {target_company}.
We detected unusual activity on your account.'

[HOOK]
'I need to verify your identity — can you confirm
your employee ID and current password?'

[RED FLAG for Awareness]
-> Legitimate staff will NEVER ask for a password over the phone.
-> Always verify by calling the official internal number back.
"""


def generate_smishing_script(target_company, pretext, short_link):
    return f"""
=== SMISHING AWARENESS SCRIPT (SMS) ===
Target Org : {target_company}
Pretext    : {pretext}

[MESSAGE]
"{target_company} Alert: {pretext}. Verify now: {short_link}
Failure to respond within 2 hours will result in account suspension."

[RED FLAG for Awareness]
-> Urgency + shortened link + threat of suspension = classic smishing pattern.
-> Never tap links in unexpected account-alert texts; go to the app/site directly.
"""


if __name__ == "__main__":
    print(generate_vishing_script("Sqrock IT", "IT Support", "Password Reset"))
    print(generate_vishing_script("National Bank", "Bank Fraud Dept.", "Suspicious Transaction"))
    print(generate_smishing_script("Sqrock IT", "Unusual login detected", "http://bit.ly/sqrock-verify"))
