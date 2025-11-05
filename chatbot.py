def chatbot_response(user_input):
    user_input = user_input.lower().strip()

    
    if any(word in user_input for word in ["hello", "hi", "hey"]):
        return "Hello! I am Symptom Checker. How can I help you today?"

    if any(word in user_input for word in ["okay","yeah", "ok", "Ohh", "oh"]):
            return "Yeah Anything else?"

    elif "how are you" in user_input:
        return "I'm doing great! How about you? Any symptoms bothering you?"

    

    disease_info = {
        "cold": ["runny nose", "sore throat", "cough", "sneezing"],
        "flu": ["fever", "chills", "muscle aches", "cough", "congestion"],
        "malaria": ["fever", "chills", "sweats", "headache","headaches", "nausea"],
        "dengue": ["high fever", "headaches","headache" "pain behind the eyes", "joint and muscle pain", "rash"],
        "covid-19": ["fever", "dry cough", "tiredness", "loss of taste or smell", "difficulty breathing"],
        "typhoid": ["high fever", "weakness", "stomach pain", "loss of appetite", "diarrhea", "constipation"],
        "influenza": ["fever", "cough", "sore throat", "runny or stuffy nose", "muscle or body aches"],
        "chickenpox": ["itchy rash", "blisters", "fever", "tiredness", "loss of appetite"],
        "pneumonia": ["cough", "cough with phlegm", "fever", "chills", "difficulty breathing", "chest pain"],
        "diabetes": ["increased thirst", "frequent urination", "extreme hunger", "unexplained weight loss", "fatigue"],
        "heartattack": ["chest pain", "shortness of breath", "pain in arms, back, neck, jaw, or stomach", "nausea", "lightheadedness"],
    }

    
    if "symptoms of" in user_input:
        disease = user_input.split("symptoms of")[-1].strip()
        if disease in disease_info:
            symptoms = disease_info[disease]
            return f"The symptoms of {disease} are: {', '.join(symptoms)}."
        else:
            return "Sorry, I don't have information about that disease."

    
    for symptom in set(sum(disease_info.values(), [])): 
         if symptom in user_input:
            related_diseases = [d for d,symptoms in disease_info.items() if symptom in symptoms]
            if related_diseases:
                return f"The symptom '{symptom}' is commonly found in: {', '.join(related_diseases)}."
            else:
                return "I couldn't find diseases related to that symptom."

    
    if "thank you" in user_input or "thanks" in user_input:
        return "You're welcome! Take care and stay healthy."

    
    return "I'm sorry, I didn't understand that. Try 'symptoms of <disease>' or 'I have <symptom>'."


while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye! Stay healthy.")
        break
    response = chatbot_response(user_input)
    print(f"Chatbot: {response}")
