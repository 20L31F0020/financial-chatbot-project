
# Financial Chatbot Prototype
# Microsoft, Tesla, Apple (2023–2025)

def financial_chatbot(user_query):
    query = user_query.lower()

    if query == "what is microsoft's total revenue?":
        return "Microsoft's average total revenue (2023–2025) was $246.23 billion."

    elif query == "what is tesla's total revenue?":
        return "Tesla's average total revenue (2023–2025) was $96.43 billion."

    elif query == "what is apple's total revenue?":
        return "Apple's average total revenue (2023–2025) was $396.83 billion."

    elif query == "which company has the highest profit margin?":
        return "Microsoft had the highest average profit margin at 35.42%."

    elif query == "which company showed the strongest growth?":
        return "Microsoft showed the strongest overall growth from 2023–2025."

    elif query == "which company is the most stable?":
        return "Apple appeared the most stable due to consistent profitability."

    elif query == "which company is the most volatile?":
        return "Tesla showed the most volatility due to stagnant revenue and declining net income."

    elif query == "help":
        return """
Available Questions:
1. What is Microsoft's total revenue?
2. What is Tesla's total revenue?
3. What is Apple's total revenue?
4. Which company has the highest profit margin?
5. Which company showed the strongest growth?
6. Which company is the most stable?
7. Which company is the most volatile?
        """

    else:
        return "Sorry, I can only answer predefined financial questions."


# Chatbot Interface
print("Welcome to the Financial Chatbot Prototype!")
print("This chatbot analyzes Microsoft, Tesla, and Apple (2023–2025).")
print("Type 'help' to see available questions.")
print("Type 'exit' to quit.\n")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chatbot: Goodbye!")
        break

    response = financial_chatbot(user_input)
    print("Chatbot:", response)
