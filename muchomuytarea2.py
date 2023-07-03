import streamlit as st

def main():
    col1, col2 = st.columns([2, 3])

    # First column with the image
    with col1:
        st.image("https://static.wixstatic.com/media/cd0557_8d06cb28d1f2423eaa6960c09add6cc0~mv2.png/v1/fill/w_214,h_214,al_c,q_85,usm_0.66_1.00_0.01,enc_auto/Untitled_design__27_-removebg-preview.png", width=114)

    # Second column with the hyperlink (using smaller text size)
    with col2:
        st.markdown("<small>[Visit us here](https://www.opportunitylanguage.com) for more.</small>", unsafe_allow_html=True)

    st.markdown("# Mucho y muy (Tarea 2)")

    st.write("\n'Mucho' se usa para cantidad o frecuencia, mientras que 'muy' se usa para intensidad o grado.\n 'Mucho' se usa con sustantivos y 'muy' con adjetivos/adverbios.")
    st.write("\nRecuerda que 'mucho' cambia según el género y número del sustantivo al que se refiere.  ")
    st.write("\nCompleta los espacios en blanco con la respuesta correcta.")
    questions = [
        ("\n¡Estoy _____ cansado después de correr cinco kilómetros hoy! ", "muy"),
        ("\nA mi hermana le gusta _____ bailar salsa en las fiestas. ", "mucho"),
        ("\nAlicia es _____ inteligente y siempre obtiene buenas calificaciones en la escuela. ", "muy"),
        ("\n¿Podrías por favor hablar _____ despacio? No entiendo bien el español. ", "muy"),
        ("\nJuan tiene _____ hambre porque no ha comido nada en todo el día. ", "mucha"),
        ("\nEl libro que leímos en clase era _____ aburrido. No pude terminarlo. ", "muy"),
        ("\nLa serie que vimos anoche fue _____ conmovedora. Todos estábamos al borde de nuestros asientos. ", "muy"),
        ("\nMi hermano estudia _____ para sus exámenes porque quiere obtener buenas notas. ", "mucho"),
        ("\nNecesito tu ayuda. Este problema de matemáticas es _____ difícil de resolver. ", "muy"),
        ("\nMi abuela cocina _____ bien. Sus comidas siempre están deliciosas. ", "muy")
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

if __name__ == "__main__":
    main()
