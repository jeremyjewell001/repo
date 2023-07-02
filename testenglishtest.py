import streamlit as st

def main():
    st.markdown("# English Test")

    st.write("\nFill in the blanks.")
    questions = [
        ("\nThe weather is ______________ today. (bueno) ", "good"),
        ("\nI _______________ to school every day. (voy) ", "go"),
        ("\nMy favorite color is _______________. (verde) ", "green"),
        ("\nMy sister is _______________ years old. (seis) ", "six"),
        ("\nThe cat is _______________ the table. (en) ", "on"),
        ("\nI _______________ watching movies in my free time. (estoy) ", "am")
    ]

    total_questions = len(questions)
    answers = []
    correct_answers = 0

    for i in range(total_questions):
        question, answer = questions[i]
        guess = st.text_input(f"Q{i+1}: {question}", key=f"question_{i+1}")
        answers.append((answer, guess))

    if st.button('Check Answers'):
        st.write("\nCheck Answers:")
        for i in range(total_questions):
            answer, guess = answers[i]
            st.write(f"Q{i+1}: {questions[i][0]}")
            st.write(f"Your answer: {guess}")
            st.write(f"Correct answer: {answer}")
            st.write("---")
            if guess.lower() == answer.lower():
                correct_answers += 1

        score = correct_answers / total_questions * 100
        st.write(f"\nTest completed. Your score: {score:.2f}%")

if __name__ == "__main__":
    main()
