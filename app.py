import streamlit as st
from sok import sok_avgang, sok_busstopp



#--side oppsett--
st.set_page_config(page_title='BUSSapp', page_icon=':oncoming_bus:')

#--Innhold:
tab1, tab2 = st.tabs(["Søk", "mine stopp"])
mineStop=[]
with tab1:
    st.subheader('Finn busstopp :bus:')
    stopp= st.text_input('Busstopp', value="", max_chars=None, key=None, type="default", help=None, autocomplete=None, on_change=None, args=None, kwargs=None, placeholder='Eks. krokensentret', disabled=False, label_visibility="hidden")
    res= sok_busstopp(stopp)
    if res:
        for r in res:
            name= r['navn']
            sted= r['sted']
            NRS_id= r['NRS_id']
            sym= ':bus:'
            click= st.expander(label= sym+ ' ' +name+ ' ' +sted)

            with click:
                avgang= sok_avgang(NRS_id)
                btn_key= NRS_id
                avganger= avgang['estimatedCalls']
                if len(avganger) == 0:
                    mes= '\tIngen avganger den neste timen'
                    st.write(mes)
                else:
                    for a in avganger:
                        rute= a['serviceJourney']['journeyPattern']['line']['id']
                        tekst= a['serviceJourney']['journeyPattern']['line']['name']
                        rute=rute.split(':')
                        rute= rute[2]
                        tid= a['expectedDepartureTime']
                        tid=tid.split('T')
                        tid= tid[1]
                        tid=tid.split('+')
                        tid=tid[0]
                        til= a['destinationDisplay']['frontText']
                        st.write(tid + '--->'+'Rute' + ' '+ rute +' '+ tekst)
                #adder= st.button('Legg til som favoritt', key=btn_key)
                #if adder:
                #    mineStop.append(NRS_id)
                    
                  
                        
with tab2:
    for m in mineStop:
        
        st.write(m)
    
    



#st.markdown(
#    """
#    <style>
#    button {
#        background: none!important;
#        border: none;
#        padding: 0!important;
#        color: white !important;
#        text-decoration: none;
#        cursor: pointer;
#        border: none !important;
#    }
#    button:hover {
#        text-decoration: none;
#        color: black !important;
#    }
#    button:focus {
#        outline: none !important;
#        box-shadow: none !important;
#        color: black !important;
#    }
#    </style>
#    """,
#    unsafe_allow_html=True,
#)