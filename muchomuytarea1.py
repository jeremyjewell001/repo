import streamlit as st

def main():
    col1, col2 = st.columns([2, 3])

    # First column with the image
    with col1:
        st.image("https://static.wixstatic.com/media/cd0557_8d06cb28d1f2423eaa6960c09add6cc0~mv2.png/v1/fill/w_214,h_214,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/Untitled_design__27_-removebg-preview.png", width=114)

    # Second column with the hyperlink (using smaller text size)
    with col2:
        st.markdown("<small>[Visit us here](https://www.opportunitylanguage.com) for more.</small>", unsafe_allow_html=True)

    st.markdown("# Mucho y muy (Tarea 1)")

    st.write("\n'Mucho' se usa para cantidad o frecuencia, mientras que 'muy' se usa para intensidad o grado.\n 'Mucho' se usa con sustantivos y 'muy' con adjetivos/adverbios.")
    st.write("\nRecuerda que 'mucho' cambia según el género y número del sustantivo al que se refiere.  ")
    st.write("\nCompleta los espacios en blanco con la respuesta correcta.")
    questions = [
        ("\nEl concierto fue __________ divertido. ", "muy"),
        ("\nMe gusta leer __________ libros de fantasía. ", "muchos"),
        ("\nAna es __________ generosa con sus amigos. ", "muy"),
        ("\nHoy hace __________ calor en la playa. ", "mucho"),
        ("\nEsta película es __________ emocionante. ", "muy"),
        ("\nPedro tiene __________ talento para la música. ", "mucho"),
        ("\nMis padres trabajan __________ horas al día. ", "muchas"),
        ("\nEl postre estaba __________ delicioso. ", "muy"),
        ("\nEn el parque hay __________ árboles y flores. ", "muchos"),
        ("\nDespués de correr me siento __________ cansado. ", "muy")
    ]

    total_questions = len(questions)
    answers = []
    correct_answers = 0

    for i in range(total_questions):
        question, answer = questions[i]
        guess = st.text_input(f"Q{i+1}: {question}", key=f"question_{i+1}")
        answers.append((answer, guess))

    if st.button('Comprueba'):
        st.write("\nComprueba:")
        for i in range(total_questions):
            answer, guess = answers[i]
            st.write(f"Q{i+1}: {questions[i][0]}")
            st.write(f"Tu respuesta: {guess}")
            st.write(f"Respuesta correcta: {answer}")
            st.write("---")
            if guess.lower() == answer.lower():
                correct_answers += 1

        score = correct_answers / total_questions * 100
        st.write(f"\nExamen completado. Tu puntuación: {score:.2f}%")
        if score == 100:
            st.markdown("[CONTINUA A LA SIGUIENTE PARTE (NEXT)](https://repo-xbdb0xjuhl9.streamlit.app/)", unsafe_allow_html=True)
        else:
            st.write("Debes responder todas las preguntas correctamente para continuar.")

if __name__ == "__main__":
    main()
