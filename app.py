from flask import Flask, jsonify, request, render_template
import pandas as pd
from joblib import load

app = Flask(__name__)

@app.route('/api/predict', methods=['GET','POST'])
def api_predict():
    """API request
    """
    if request.method == 'POST':  #this block is only entered when the form is submitted
        Modelo = load('ReactividadVIH.joblib')
        req_data = request.get_json () 
        if not req_data:
            return jsonify(error="request body cannot be empty"), 400
        ES_01 = 0 
        ES_02 = 0 
        ES_03 = 0
        ES_04 = 0
        TB_01 = 0
        MA_01 = 0
        MA_02 = 0
        MA_03 = 0
        MA_04 = 0
        MA_05 = 0
        MA_06 = 0
        MA_07 = 0
        MA_08 = 0
        MA_09 = 0
        MA_10 = 0
        MA_11 = 0
        LA_01 = 0
        LA_02 = 0
        LA_03 = 0
        LA_04 = 0
        LA_05 = 0
        LA_06 = 0
        LA_07 = 0
        LA_08 = 0
        LA_09 = 0
        LA_10 = 0
        LA_11 = 0
        TD_01 = 0
        TD_02 = 0
        TD_03 = 0
        TD_04 = 0
        TP_01 = 0
        TP_02 = 0
        TP_03 = 0
        TP_04 = 0
        TP_05 = 0
        TP_06 = 0
        TP_07 = 0
        TN_01 = 0

        TB_01 = 0
        LA_01,LA_02,LA_03,LA_04,LA_05,LA_06,LA_07,LA_08,LA_09,LA_10,LA_11 = (0,0,0,0,0,0,0,0,0,0,0)
        MA_01,MA_02,MA_03,MA_04,MA_05,MA_06,MA_07,MA_08,MA_09,MA_10,MA_11 = (0,0,0,0,0,0,0,0,0,0,0)
        TN_01 = 0
        TD_01,TD_02,TD_03,TD_04 = (0,0,0,0)
        TP_01,TP_02,TP_03,TP_04,TP_05,TP_06,TP_07 = (0,0,0,0,0,0,0)
        ES_01,ES_02,ES_03,ES_04 = (0,0,0,0)

        tipo_brigada = req_data['tipo_brigada']
        lugar_abordaje = req_data['lugar_abordaje']
        mes_abordado = req_data['mes_abordado']
        tipo_nacionalidad = req_data['tipo_nacionalidad']
        tipo_documento = req_data['tipo_documento']
        tipo_poblacion = req_data['tipo_poblacion']
        estrato_social = req_data['estrato_social']

        features = { 
            'tipo_brigada': tipo_brigada,
            'lugar_abordaje': lugar_abordaje,
            'mes_abordado': mes_abordado,
            'tipo_nacionalidad': tipo_nacionalidad,
            'tipo_documento': tipo_documento,
            'tipo_poblacion': tipo_poblacion,
            'estrato_social': estrato_social
        }

        if tipo_brigada == '1':
            TB_01 = 1
        if tipo_brigada == '2':
            TB_01 = 0

        if lugar_abordaje == '1':
            LA_01,LA_02,LA_03,LA_04,LA_05,LA_06,LA_07,LA_08,LA_09,LA_10,LA_11 = (1,0,0,0,0,0,0,0,0,0,0)
        if lugar_abordaje == '2':
            LA_01,LA_02,LA_03,LA_04,LA_05,LA_06,LA_07,LA_08,LA_09,LA_10,LA_11 = (0,1,0,0,0,0,0,0,0,0,0)
        if lugar_abordaje == '3':
            LA_01,LA_02,LA_03,LA_04,LA_05,LA_06,LA_07,LA_08,LA_09,LA_10,LA_11 = (0,0,1,0,0,0,0,0,0,0,0)
        if lugar_abordaje == '4':
            LA_01,LA_02,LA_03,LA_04,LA_05,LA_06,LA_07,LA_08,LA_09,LA_10,LA_11 = (0,0,0,1,0,0,0,0,0,0,0)
        if lugar_abordaje == '5':
            LA_01,LA_02,LA_03,LA_04,LA_05,LA_06,LA_07,LA_08,LA_09,LA_10,LA_11 = (0,0,0,0,1,0,0,0,0,0,0)
        if lugar_abordaje == '6':
            LA_01,LA_02,LA_03,LA_04,LA_05,LA_06,LA_07,LA_08,LA_09,LA_10,LA_11 = (0,0,0,0,0,1,0,0,0,0,0)
        if lugar_abordaje == '7':
            LA_01,LA_02,LA_03,LA_04,LA_05,LA_06,LA_07,LA_08,LA_09,LA_10,LA_11 = (0,0,0,0,0,0,1,0,0,0,0)
        if lugar_abordaje == '8':
            LA_01,LA_02,LA_03,LA_04,LA_05,LA_06,LA_07,LA_08,LA_09,LA_10,LA_11 = (0,0,0,0,0,0,0,1,0,0,0)
        if lugar_abordaje == '9':
            LA_01,LA_02,LA_03,LA_04,LA_05,LA_06,LA_07,LA_08,LA_09,LA_10,LA_11 = (0,0,0,0,0,0,0,0,1,0,0)
        if lugar_abordaje == '10':
            LA_01,LA_02,LA_03,LA_04,LA_05,LA_06,LA_07,LA_08,LA_09,LA_10,LA_11 = (0,0,0,0,0,0,0,0,0,1,0)
        if lugar_abordaje == '11':
            LA_01,LA_02,LA_03,LA_04,LA_05,LA_06,LA_07,LA_08,LA_09,LA_10,LA_11 = (0,0,0,0,0,0,0,0,0,0,1)
        if lugar_abordaje == '12':
            LA_01,LA_02,LA_03,LA_04,LA_05,LA_06,LA_07,LA_08,LA_09,LA_10,LA_11 = (0,0,0,0,0,0,0,0,0,0,0)

        if mes_abordado == '1':
            MA_01,MA_02,MA_03,MA_04,MA_05,MA_06,MA_07,MA_08,MA_09,MA_10,MA_11 = (1,0,0,0,0,0,0,0,0,0,0)
        if mes_abordado == '2':
            MA_01,MA_02,MA_03,MA_04,MA_05,MA_06,MA_07,MA_08,MA_09,MA_10,MA_11 = (0,1,0,0,0,0,0,0,0,0,0)
        if mes_abordado == '3':
            MA_01,MA_02,MA_03,MA_04,MA_05,MA_06,MA_07,MA_08,MA_09,MA_10,MA_11 = (0,0,1,0,0,0,0,0,0,0,0)
        if mes_abordado == '4':
            MA_01,MA_02,MA_03,MA_04,MA_05,MA_06,MA_07,MA_08,MA_09,MA_10,MA_11 = (0,0,0,1,0,0,0,0,0,0,0)
        if mes_abordado == '5':
            MA_01,MA_02,MA_03,MA_04,MA_05,MA_06,MA_07,MA_08,MA_09,MA_10,MA_11 = (0,0,0,0,1,0,0,0,0,0,0)
        if mes_abordado == '6':
            MA_01,MA_02,MA_03,MA_04,MA_05,MA_06,MA_07,MA_08,MA_09,MA_10,MA_11 = (0,0,0,0,0,1,0,0,0,0,0)
        if mes_abordado == '7':
            MA_01,MA_02,MA_03,MA_04,MA_05,MA_06,MA_07,MA_08,MA_09,MA_10,MA_11 = (0,0,0,0,0,0,1,0,0,0,0)
        if mes_abordado == '8':
            MA_01,MA_02,MA_03,MA_04,MA_05,MA_06,MA_07,MA_08,MA_09,MA_10,MA_11 = (0,0,0,0,0,0,0,1,0,0,0)
        if mes_abordado == '9':
            MA_01,MA_02,MA_03,MA_04,MA_05,MA_06,MA_07,MA_08,MA_09,MA_10,MA_11 = (0,0,0,0,0,0,0,0,1,0,0)
        if mes_abordado == '10':
            MA_01,MA_02,MA_03,MA_04,MA_05,MA_06,MA_07,MA_08,MA_09,MA_10,MA_11 = (0,0,0,0,0,0,0,0,0,1,0)
        if mes_abordado == '11':
            MA_01,MA_02,MA_03,MA_04,MA_05,MA_06,MA_07,MA_08,MA_09,MA_10,MA_11 = (0,0,0,0,0,0,0,0,0,0,1)
        if mes_abordado == '12':
            MA_01,MA_02,MA_03,MA_04,MA_05,MA_06,MA_07,MA_08,MA_09,MA_10,MA_11 = (0,0,0,0,0,0,0,0,0,0,0)

        if tipo_nacionalidad == '1':
            TN_01 = 1
        if tipo_nacionalidad == '2':
            TN_01 = 0

        if tipo_documento == '1':
            TD_01,TD_02,TD_03,TD_04 = (1,0,0,0)
        if tipo_documento == '2':
            TD_01,TD_02,TD_03,TD_04 = (0,1,0,0)
        if tipo_documento == '3':
            TD_01,TD_02,TD_03,TD_04 = (0,0,1,0)
        if tipo_documento == '4':
            TD_01,TD_02,TD_03,TD_04 = (0,0,0,1)
        if tipo_documento == '5':
            TD_01,TD_02,TD_03,TD_04 = (0,0,0,0)

        if tipo_poblacion == '1':
            TP_01,TP_02,TP_03,TP_04,TP_05,TP_06,TP_07 = (1,0,0,0,0,0,0)
        if tipo_poblacion == '2':
            TP_01,TP_02,TP_03,TP_04,TP_05,TP_06,TP_07 = (0,1,0,0,0,0,0)
        if tipo_poblacion == '3':
            TP_01,TP_02,TP_03,TP_04,TP_05,TP_06,TP_07 = (0,0,1,0,0,0,0)
        if tipo_poblacion == '4':
            TP_01,TP_02,TP_03,TP_04,TP_05,TP_06,TP_07 = (0,0,0,1,0,0,0)
        if tipo_poblacion == '5':
            TP_01,TP_02,TP_03,TP_04,TP_05,TP_06,TP_07 = (0,0,0,0,1,0,0)
        if tipo_poblacion == '6':
            TP_01,TP_02,TP_03,TP_04,TP_05,TP_06,TP_07 = (0,0,0,0,0,1,0)
        if tipo_poblacion == '7':
            TP_01,TP_02,TP_03,TP_04,TP_05,TP_06,TP_07 = (0,0,0,0,0,0,1)
        if tipo_poblacion == '8':
            TP_01,TP_02,TP_03,TP_04,TP_05,TP_06,TP_07 = (0,0,0,0,0,0,0)

        if estrato_social == '1':
            ES_01,ES_02,ES_03,ES_04 = (1,0,0,0)
        if estrato_social == '2':
            ES_01,ES_02,ES_03,ES_04 = (0,1,0,0)
        if estrato_social == '3':
            ES_01,ES_02,ES_03,ES_04 = (0,0,1,0)
        if estrato_social == '4':
            ES_01,ES_02,ES_03,ES_04 = (0,0,0,1)
        if estrato_social == '5':
            ES_01,ES_02,ES_03,ES_04 = (0,0,0,0)

        Xnew = [ES_01, ES_02, ES_03, ES_04, TB_01, MA_01, MA_02,
                MA_03, MA_04, MA_05, MA_06, MA_07, MA_08, MA_09,
                MA_10, MA_11, LA_01, LA_02, LA_03, LA_04, LA_05,
                LA_06, LA_07, LA_08, LA_09, LA_10, LA_11, TD_01,
                TD_02, TD_03, TD_04, TP_01, TP_02, TP_03, TP_04,
                TP_05, TP_06, TP_07, TN_01]        

        dataXnewValues = [['ES_01', 'ES_02', 'ES_03', 'ES_04', 'TB_01', 'MA_01', 'MA_02',
                           'MA_03', 'MA_04', 'MA_05', 'MA_06', 'MA_07', 'MA_08', 'MA_09',
                           'MA_10', 'MA_11', 'LA_01', 'LA_02', 'LA_03', 'LA_04', 'LA_05',
                           'LA_06', 'LA_07', 'LA_08', 'LA_09', 'LA_10', 'LA_11', 'TD_01',
                           'TD_02', 'TD_03', 'TD_04', 'TP_01', 'TP_02', 'TP_03', 'TP_04',
                           'TP_05', 'TP_06', 'TP_07', 'TN_01'], Xnew]

        dataXnewColumns = dataXnewValues.pop(0)

        dataXnewDf = pd.DataFrame(dataXnewValues, columns=dataXnewColumns)

        Ynew = Modelo.predict(dataXnewDf)

        if Ynew[0] == 1:
            Mensaje = 'Alta probabilidad de Reactividad Positiva en la Prueba de VIH'
        else:
            Mensaje = 'Alta probabilidad de Reactividad Negativa en la Prueba de VIH'

        return jsonify( inputs=features,predictions=Mensaje)

    return '''User postman u otro cliente para ejecutar esta API REST'''

@app.route('/', methods=['GET','POST'])
def predict():
    """
    """
    if request.method == 'POST':  #this block is only entered when the form is submitted
        Modelo = load('ReactividadVIH.joblib')
        ES_01 = 0 
        ES_02 = 0 
        ES_03 = 0
        ES_04 = 0
        TB_01 = 0
        MA_01 = 0
        MA_02 = 0
        MA_03 = 0
        MA_04 = 0
        MA_05 = 0
        MA_06 = 0
        MA_07 = 0
        MA_08 = 0
        MA_09 = 0
        MA_10 = 0
        MA_11 = 0
        LA_01 = 0
        LA_02 = 0
        LA_03 = 0
        LA_04 = 0
        LA_05 = 0
        LA_06 = 0
        LA_07 = 0
        LA_08 = 0
        LA_09 = 0
        LA_10 = 0
        LA_11 = 0
        TD_01 = 0
        TD_02 = 0
        TD_03 = 0
        TD_04 = 0
        TP_01 = 0
        TP_02 = 0
        TP_03 = 0
        TP_04 = 0
        TP_05 = 0
        TP_06 = 0
        TP_07 = 0
        TN_01 = 0

        TB_01 = 0
        LA_01,LA_02,LA_03,LA_04,LA_05,LA_06,LA_07,LA_08,LA_09,LA_10,LA_11 = (0,0,0,0,0,0,0,0,0,0,0)
        MA_01,MA_02,MA_03,MA_04,MA_05,MA_06,MA_07,MA_08,MA_09,MA_10,MA_11 = (0,0,0,0,0,0,0,0,0,0,0)
        TN_01 = 0
        TD_01,TD_02,TD_03,TD_04 = (0,0,0,0)
        TP_01,TP_02,TP_03,TP_04,TP_05,TP_06,TP_07 = (0,0,0,0,0,0,0)
        ES_01,ES_02,ES_03,ES_04 = (0,0,0,0)

        tipo_brigada = request.form.get('tipo_brigada')
        lugar_abordaje = request.form.get('lugar_abordaje')
        mes_abordado = request.form.get('mes_abordado')
        tipo_nacionalidad = request.form.get('tipo_nacionalidad')
        tipo_documento = request.form.get('tipo_documento')
        tipo_poblacion = request.form.get('tipo_poblacion')
        estrato_social = request.form.get('estrato_social')

        features = { 
            'tipo_brigada': tipo_brigada,
            'lugar_abordaje': lugar_abordaje,
            'mes_abordado': mes_abordado,
            'tipo_nacionalidad': tipo_nacionalidad,
            'tipo_documento': tipo_documento,
            'tipo_poblacion': tipo_poblacion,
            'estrato_social': estrato_social
        }

        if tipo_brigada == '1':
            TB_01 = 1
        if tipo_brigada == '2':
            TB_01 = 0

        if lugar_abordaje == '1':
            LA_01,LA_02,LA_03,LA_04,LA_05,LA_06,LA_07,LA_08,LA_09,LA_10,LA_11 = (1,0,0,0,0,0,0,0,0,0,0)
        if lugar_abordaje == '2':
            LA_01,LA_02,LA_03,LA_04,LA_05,LA_06,LA_07,LA_08,LA_09,LA_10,LA_11 = (0,1,0,0,0,0,0,0,0,0,0)
        if lugar_abordaje == '3':
            LA_01,LA_02,LA_03,LA_04,LA_05,LA_06,LA_07,LA_08,LA_09,LA_10,LA_11 = (0,0,1,0,0,0,0,0,0,0,0)
        if lugar_abordaje == '4':
            LA_01,LA_02,LA_03,LA_04,LA_05,LA_06,LA_07,LA_08,LA_09,LA_10,LA_11 = (0,0,0,1,0,0,0,0,0,0,0)
        if lugar_abordaje == '5':
            LA_01,LA_02,LA_03,LA_04,LA_05,LA_06,LA_07,LA_08,LA_09,LA_10,LA_11 = (0,0,0,0,1,0,0,0,0,0,0)
        if lugar_abordaje == '6':
            LA_01,LA_02,LA_03,LA_04,LA_05,LA_06,LA_07,LA_08,LA_09,LA_10,LA_11 = (0,0,0,0,0,1,0,0,0,0,0)
        if lugar_abordaje == '7':
            LA_01,LA_02,LA_03,LA_04,LA_05,LA_06,LA_07,LA_08,LA_09,LA_10,LA_11 = (0,0,0,0,0,0,1,0,0,0,0)
        if lugar_abordaje == '8':
            LA_01,LA_02,LA_03,LA_04,LA_05,LA_06,LA_07,LA_08,LA_09,LA_10,LA_11 = (0,0,0,0,0,0,0,1,0,0,0)
        if lugar_abordaje == '9':
            LA_01,LA_02,LA_03,LA_04,LA_05,LA_06,LA_07,LA_08,LA_09,LA_10,LA_11 = (0,0,0,0,0,0,0,0,1,0,0)
        if lugar_abordaje == '10':
            LA_01,LA_02,LA_03,LA_04,LA_05,LA_06,LA_07,LA_08,LA_09,LA_10,LA_11 = (0,0,0,0,0,0,0,0,0,1,0)
        if lugar_abordaje == '11':
            LA_01,LA_02,LA_03,LA_04,LA_05,LA_06,LA_07,LA_08,LA_09,LA_10,LA_11 = (0,0,0,0,0,0,0,0,0,0,1)
        if lugar_abordaje == '12':
            LA_01,LA_02,LA_03,LA_04,LA_05,LA_06,LA_07,LA_08,LA_09,LA_10,LA_11 = (0,0,0,0,0,0,0,0,0,0,0)

        if mes_abordado == '1':
            MA_01,MA_02,MA_03,MA_04,MA_05,MA_06,MA_07,MA_08,MA_09,MA_10,MA_11 = (1,0,0,0,0,0,0,0,0,0,0)
        if mes_abordado == '2':
            MA_01,MA_02,MA_03,MA_04,MA_05,MA_06,MA_07,MA_08,MA_09,MA_10,MA_11 = (0,1,0,0,0,0,0,0,0,0,0)
        if mes_abordado == '3':
            MA_01,MA_02,MA_03,MA_04,MA_05,MA_06,MA_07,MA_08,MA_09,MA_10,MA_11 = (0,0,1,0,0,0,0,0,0,0,0)
        if mes_abordado == '4':
            MA_01,MA_02,MA_03,MA_04,MA_05,MA_06,MA_07,MA_08,MA_09,MA_10,MA_11 = (0,0,0,1,0,0,0,0,0,0,0)
        if mes_abordado == '5':
            MA_01,MA_02,MA_03,MA_04,MA_05,MA_06,MA_07,MA_08,MA_09,MA_10,MA_11 = (0,0,0,0,1,0,0,0,0,0,0)
        if mes_abordado == '6':
            MA_01,MA_02,MA_03,MA_04,MA_05,MA_06,MA_07,MA_08,MA_09,MA_10,MA_11 = (0,0,0,0,0,1,0,0,0,0,0)
        if mes_abordado == '7':
            MA_01,MA_02,MA_03,MA_04,MA_05,MA_06,MA_07,MA_08,MA_09,MA_10,MA_11 = (0,0,0,0,0,0,1,0,0,0,0)
        if mes_abordado == '8':
            MA_01,MA_02,MA_03,MA_04,MA_05,MA_06,MA_07,MA_08,MA_09,MA_10,MA_11 = (0,0,0,0,0,0,0,1,0,0,0)
        if mes_abordado == '9':
            MA_01,MA_02,MA_03,MA_04,MA_05,MA_06,MA_07,MA_08,MA_09,MA_10,MA_11 = (0,0,0,0,0,0,0,0,1,0,0)
        if mes_abordado == '10':
            MA_01,MA_02,MA_03,MA_04,MA_05,MA_06,MA_07,MA_08,MA_09,MA_10,MA_11 = (0,0,0,0,0,0,0,0,0,1,0)
        if mes_abordado == '11':
            MA_01,MA_02,MA_03,MA_04,MA_05,MA_06,MA_07,MA_08,MA_09,MA_10,MA_11 = (0,0,0,0,0,0,0,0,0,0,1)
        if mes_abordado == '12':
            MA_01,MA_02,MA_03,MA_04,MA_05,MA_06,MA_07,MA_08,MA_09,MA_10,MA_11 = (0,0,0,0,0,0,0,0,0,0,0)

        if tipo_nacionalidad == '1':
            TN_01 = 1
        if tipo_nacionalidad == '2':
            TN_01 = 0

        if tipo_documento == '1':
            TD_01,TD_02,TD_03,TD_04 = (1,0,0,0)
        if tipo_documento == '2':
            TD_01,TD_02,TD_03,TD_04 = (0,1,0,0)
        if tipo_documento == '3':
            TD_01,TD_02,TD_03,TD_04 = (0,0,1,0)
        if tipo_documento == '4':
            TD_01,TD_02,TD_03,TD_04 = (0,0,0,1)
        if tipo_documento == '5':
            TD_01,TD_02,TD_03,TD_04 = (0,0,0,0)

        if tipo_poblacion == '1':
            TP_01,TP_02,TP_03,TP_04,TP_05,TP_06,TP_07 = (1,0,0,0,0,0,0)
        if tipo_poblacion == '2':
            TP_01,TP_02,TP_03,TP_04,TP_05,TP_06,TP_07 = (0,1,0,0,0,0,0)
        if tipo_poblacion == '3':
            TP_01,TP_02,TP_03,TP_04,TP_05,TP_06,TP_07 = (0,0,1,0,0,0,0)
        if tipo_poblacion == '4':
            TP_01,TP_02,TP_03,TP_04,TP_05,TP_06,TP_07 = (0,0,0,1,0,0,0)
        if tipo_poblacion == '5':
            TP_01,TP_02,TP_03,TP_04,TP_05,TP_06,TP_07 = (0,0,0,0,1,0,0)
        if tipo_poblacion == '6':
            TP_01,TP_02,TP_03,TP_04,TP_05,TP_06,TP_07 = (0,0,0,0,0,1,0)
        if tipo_poblacion == '7':
            TP_01,TP_02,TP_03,TP_04,TP_05,TP_06,TP_07 = (0,0,0,0,0,0,1)
        if tipo_poblacion == '8':
            TP_01,TP_02,TP_03,TP_04,TP_05,TP_06,TP_07 = (0,0,0,0,0,0,0)

        if estrato_social == '1':
            ES_01,ES_02,ES_03,ES_04 = (1,0,0,0)
        if estrato_social == '2':
            ES_01,ES_02,ES_03,ES_04 = (0,1,0,0)
        if estrato_social == '3':
            ES_01,ES_02,ES_03,ES_04 = (0,0,1,0)
        if estrato_social == '4':
            ES_01,ES_02,ES_03,ES_04 = (0,0,0,1)
        if estrato_social == '5':
            ES_01,ES_02,ES_03,ES_04 = (0,0,0,0)

        Xnew = [ES_01, ES_02, ES_03, ES_04, TB_01, MA_01, MA_02,
                MA_03, MA_04, MA_05, MA_06, MA_07, MA_08, MA_09,
                MA_10, MA_11, LA_01, LA_02, LA_03, LA_04, LA_05,
                LA_06, LA_07, LA_08, LA_09, LA_10, LA_11, TD_01,
                TD_02, TD_03, TD_04, TP_01, TP_02, TP_03, TP_04,
                TP_05, TP_06, TP_07, TN_01]        

        dataXnewValues = [['ES_01', 'ES_02', 'ES_03', 'ES_04', 'TB_01', 'MA_01', 'MA_02',
                           'MA_03', 'MA_04', 'MA_05', 'MA_06', 'MA_07', 'MA_08', 'MA_09',
                           'MA_10', 'MA_11', 'LA_01', 'LA_02', 'LA_03', 'LA_04', 'LA_05',
                           'LA_06', 'LA_07', 'LA_08', 'LA_09', 'LA_10', 'LA_11', 'TD_01',
                           'TD_02', 'TD_03', 'TD_04', 'TP_01', 'TP_02', 'TP_03', 'TP_04',
                           'TP_05', 'TP_06', 'TP_07', 'TN_01'], Xnew]

        dataXnewColumns = dataXnewValues.pop(0)

        dataXnewDf = pd.DataFrame(dataXnewValues, columns=dataXnewColumns)

        Ynew = Modelo.predict(dataXnewDf)

        if Ynew[0] == 1:
            Mensaje = 'Paciente con alta probabilidad de tener Reactividad Positiva en su Prueba de VIH'
        else:
            Mensaje = 'Paciente con alta probabilidad de tener Reactividad Negativa en su Prueba de VIH'
        return render_template("index.html", inputs=features, predictions=Mensaje, 
            tipo_brigada=tipo_brigada, lugar_abordaje=lugar_abordaje, 
            mes_abordado=mes_abordado, tipo_nacionalidad=tipo_nacionalidad, 
            tipo_documento=tipo_documento, tipo_poblacion=tipo_poblacion, 
            estrato_social=estrato_social)

        tipo_brigada = request.form.get('tipo_brigada')
        lugar_abordaje = request.form.get('lugar_abordaje')
        mes_abordado = request.form.get('mes_abordado')
        tipo_nacionalidad = request.form.get('tipo_nacionalidad')
        tipo_documento = request.form.get('tipo_documento')
        tipo_poblacion = request.form.get('tipo_poblacion')
        estrato_social = request.form.get('estrato_social')

    return render_template("index.html")
