# Mapping Dictionary
REJECTION_REASONS_MAP = {
    "Fake_document": "Fake_document",
    "Not_Covered": "Not_Covered",
    "Policy_expired": "Policy_expired"
}

# Function 1: Error Handler
def handle_error(error_message):
    print(f"Error: {error_message}")
    return "Error"

# Function 2: Keyword Match Checker
def contains_rejection_reason(rejection_text, reason):
    try:
        if rejection_text and isinstance(rejection_text, str):
            return reason.lower() in rejection_text.lower()
    except Exception as e:
        handle_error(f"Error in contains_rejection_reason: {str(e)}")
    return False

# Function 3: Map Rejection Reason
def map_rejection_reason(rejection_text):
    try:
        if rejection_text and isinstance(rejection_text, str):
            for reason, rejection_class in REJECTION_REASONS_MAP.items():
                if contains_rejection_reason(rejection_text, reason):
                    return rejection_class
            return "Unknown"
        else:
            return "No Remark"
    except Exception as e:
        handle_error(f"Error in map_rejection_reason: {str(e)}")
        return "Error"

# Function 4: Main Classifier
def complex_rejection_classifier(remark_text):
    try:
        if remark_text is None or not isinstance(remark_text, str) or len(remark_text.strip()) == 0:
            return "NoRemark"

        
        fake_doc = contains_rejection_reason(remark_text, "Fake_document")
        not_covered = contains_rejection_reason(remark_text, "Not_Covered")
        policy_expired = contains_rejection_reason(remark_text, "Policy_expired")

        if fake_doc:
            return "Fake_document"
        elif not_covered:
            return "Not_Covered"
        elif policy_expired:
            return "Policy_expired"
        else:
            return map_rejection_reason(remark_text)

    except Exception as e:
        handle_error(f"Error in complex_rejection_classifier: {str(e)}")
        return "Error"
