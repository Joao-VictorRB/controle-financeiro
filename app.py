from streamlit import  streamlit as st 
import pandas as pd
import plotly.express as px

menu = st.sidebar.selectbox("Selecione uma Opção", ["Home", "Adicionar Ganhos", "Adicionar Despesas", "Ver Resumo"])

if menu == "Home":
    pass




elif menu == "Adicionar Ganhos":
    
    st.markdown("<h1 style='text-align: center; padding-bottom:4rem;'>💲Adicionar Ganhos💲</h1>", unsafe_allow_html=True)


    col1,col2 = st.columns(2, gap="large", vertical_alignment="top")

    with col1:

        with st.form(key='ganhos_form', clear_on_submit=True, enter_to_submit=False, border=False ):
            salario = st.number_input("Salário", min_value=0.0, step=100.0, format="%.2f")
            rendaExtra = st.number_input("Renda Extra", min_value=0.0, step=100.0, format="%.2f")
            valeRefeicao = st.number_input("Vale Refeição",min_value=0.0, step=100.0, format="%.2f")
            somar_ganhos = salario + rendaExtra + valeRefeicao
            enviar_ganhos = st.form_submit_button("Enviar Ganhos", use_container_width=True)

  
            
    with col2:
        st.markdown("<h2 style='text-align: center; padding-bottom:2.3rem; padding-top:3.8rem;'>👇🏽Renda Total👇🏽</h2>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align: center; pading-right:10px; background-color:#1E1E1E;border-radius:2rem;'>R$ {somar_ganhos:.2f}</h3>", unsafe_allow_html=True)
                    
               
    if enviar_ganhos:   

        df_ganhos = pd.DataFrame({
                'Tipo':['Salário', 'Renda Extra', 'Vale Refeição'],
                'Valor':[salario,rendaExtra,valeRefeicao]
                })
        Titulo = st.markdown("<h2 style='text-align: center; padding-top:3.5rem;'>Gráfico</h2>", unsafe_allow_html=True)

        fig = px.pie(
        df_ganhos,
        names='Tipo',
        values='Valor',
        )

        fig.update_traces(
        textinfo='label+percent+value',
        textfont_size=12,
        marker=dict(colors=['#1f77b4', '#2ca02c', '#ff7f0e'])
        )
        fig.update_layout(
            legend_orientation="h",
            legend_y = -0.1,
            legend_x = 0.5,
            legend_xanchor = "center",
        )
    
        st.plotly_chart(fig)










elif menu == "Adicionar Despesas":
    
    st.markdown("<h1 style='text-align: center; margin-bottom:3rem;'>😭Adicionar Despesas😭</h1>", unsafe_allow_html=True)

    col3,col4 = st.columns(2, gap="large", vertical_alignment="top")
    
    with st.form(key='despesasFixa_form', clear_on_submit=True, enter_to_submit=False, border=False ):
            with col3:
                st.markdown("<h3 style='text-align: center; margin-bottom:.5rem;'>Despesas Fixas</h3>", unsafe_allow_html=True)
                faculdade = st.number_input("Faculdade", min_value=0.0, step=100.0, format="%.2f")
                academia = st.number_input("Academia", min_value=0.0, step=100.0, format="%.2f")
                convenio = st.number_input("Convênio",min_value=0.0, step=100.0, format="%.2f")
            with col4:
                st.markdown("<h3 style='text-align: center; margin-bottom:.5rem;'>Despesas Variáveis</h3>", unsafe_allow_html=True)
                vestuario = st.number_input("Vestuário", min_value=0.0, step=100.0, format="%.2f")
                cursos = st.number_input("Cursos", min_value=0.0, step=100.0, format="%.2f")
                diversao = st.number_input("Diversão",min_value=0.0, step=100.0, format="%.2f")
  
            somar_gastosFixo = faculdade + convenio + academia
            somar_gastosVariaveis = vestuario + cursos + diversao
            somar_gastos = somar_gastosFixo + somar_gastosVariaveis

            enviar_gastos = st.form_submit_button("Enviar Gastos", use_container_width=True)

            
    col5,col6 = st.columns(2, gap="large", vertical_alignment="top")        
  
    with col5:  
        st.markdown("<h2 style='text-align: center; padding-bottom:6rem; padding-top:3.8rem;'>👇🏽Gastos Total👇🏽</h2>", unsafe_allow_html=True)
        st.markdown(f"<h3 style='text-align: center; pading-right:10px; background-color:#1E1E1E;border-radius:2rem;'>R$ {somar_gastos:.2f}</h3>", unsafe_allow_html=True)

    with col6:
        if enviar_gastos:   

            df_gastos_totais = pd.DataFrame({
                    'Tipo':['Faculdade', 'academia', 'Convênio', 'Vestuário', 'Cursos', 'Diversão'],
                    'Valor':[faculdade, academia, convenio, vestuario, cursos, diversao]
                    })
            Titulo = st.markdown("<h2 style='text-align: center; padding-top:3.5rem;'>Gráfico</h2>", unsafe_allow_html=True)

            fig = px.pie(
            df_gastos_totais,
            names='Tipo',
            values='Valor',
            )

            fig.update_traces(
            textinfo='label+percent+value',
            textfont_size=12,
             marker=dict(colors=['#1f77b4','#2ca02c','#d62728','#9467bd','#ff7f0e','#17becf'])
            )
            fig.update_layout(
                legend_orientation="h",
                legend_y = -0.1,
                legend_x = 0.5,
                legend_xanchor = "center",
            )
        
            st.plotly_chart(fig)


else:
    pass