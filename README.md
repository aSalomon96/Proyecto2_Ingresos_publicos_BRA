# Proyecto2_Ingresos_publicos_BRA 📊 

### **Descripción del Proyecto** 📝​

Este proyecto tiene como objetivo analizar la discrepancia entre los valores presupuestados, recaudados y ejecutados por diferentes ministerios a lo largo de un periodo determinado, proporcionando insights clave sobre la eficiencia en la planificación y ejecución financiera. A través del uso de técnicas analíticas y visualización de datos, se busca identificar patrones, anomalías y oportunidades de mejora en la gestión de ingresos gubernamentales.

- **El análisis incluye:** 

    - Comparación de Presupuestos Previstos y Recaudados:
Examina la diferencia entre los valores proyectados y los realmente obtenidos para identificar factores que afectan la precisión de las estimaciones.

    - Evaluación del Porcentaje de Cumplimiento:
Analiza el grado de cumplimiento presupuestario para cada ministerio y categoría de ingresos, destacando áreas con sobrecumplimiento o incumplimiento significativo.

    - Exploración de Valores Lanzados y Rendición de Cuentas:
Investiga los valores declarados como devengados para evaluar la consistencia y transparencia en la asignación de recursos.

    - Identificación de Outliers y Errores Contables:
Detecta datos inusuales, como valores negativos o inconsistencias, que pueden impactar el balance general y la credibilidad del presupuesto.

    - Tendencias Temporales y Análisis Interanual:
Estudia la evolución de ingresos previstos y recaudados a lo largo del tiempo, destacando el impacto de eventos extraordinarios, como crisis económicas o cambios en políticas fiscales.

### - **Estructura del Proyecto** 🗂️

        ├── datos
            ├── output_data                         
                ├── df_limpio.pkl                   # data limpia y unificada
            ├── raw_data                            # data sin modificar en .gitignore
        ├── src
            ├── _pycache_       
            ├── fx_limpieza.py                      # funcion para limpiar dataframe
        ├── tratamiento
            ├── 01_Union_y_limpieza_datos.ipynb     # Limpieza y exportacion de archivo .pkl
            ├── 02_EDAs.ipynb                       # Analisis del proyecto
            ├── 03_Conclusiones.ipynb               # Coclusiones del proyecto   
        ├── gitignore                               # Se agrego gitignore para que no se suban los CSV que pesaban mucho
        ├── README.md                               # Descripción del proyecto                                

### - **Instalación y Requisitos** 🛠️

Este proyecto usa Python 3.9 🐍 y requiere las siguientes librerías:

    - pandas 
    - matplotlib
    - seaborn 
    - sys 

### - **Limpieza de datos**🧹

La limpieza de datos fue un paso crítico para garantizar la calidad y consistencia del análisis. Se realizaron las siguientes acciones principales:

- Manejo de Valores Nulos:
Se encontraron valores nulos únicamente en la columna de "fecha de ejecución". Estos valores fueron imputados reemplazándolos con el 1 de enero del año correspondiente, obtenido de una columna adyacente.
Las columnas relacionadas con valores numéricos o de tipo float mostraban valores iguales a cero en algunos casos. Estos se conservaron, ya que podrían representar datos válidos.

- Eliminación de Duplicados:
No se identificaron registros duplicados en el DataFrame, lo que garantiza que cada registro es único.
Renombrado de Columnas:

- Se renombraron las columnas para reducir barreras de lenguaje y facilitar su comprensión, adoptando nombres más claros y descriptivos.

- Conversión de Tipos de Datos:
Las columnas categóricas fueron convertidas a un formato numérico donde correspondía, para permitir análisis cuantitativos.
Las columnas de tipo fecha fueron transformadas al formato datetime64 para facilitar análisis temporales.

- Revisión de Datos:
Se verificaron los valores nulos por columna, confirmando la integridad de los datos después del proceso de limpieza.
Los tipos de datos quedaron distribuidos en: 4 columnas numéricas enteras (int64), 4 columnas numéricas flotantes (float64), 7 categóricas (object), y 1 columna de fecha (datetime64[ns]).

- #### *Insights Post-Limpieza*:

El DataFrame cuenta con 1,026,299 registros y 16 columnas, representando información detallada sobre la recaudación y ejecución presupuestaria de diversos ministerios.
Tras la limpieza, todas las columnas contienen datos completos, lo que asegura un análisis más preciso.
La estructura del DataFrame optimizada ocupa 125.3+ KB en memoria, permitiendo un manejo eficiente de los datos durante el análisis.

### - **Resultados y Conclusiones** 🕵️‍♂️

El análisis de los datos de planificación y ejecución presupuestaria en el período 2013-2021 reveló patrones importantes en las tendencias de ingresos y gastos del gobierno. Aunque se observan avances como el crecimiento de valores recaudados y superávits recientes en ciertas áreas, persisten desafíos estructurales en la planificación y ejecución financiera.

### *Aspectos Clave del Análisis*

1. #### Tendencias Generales:
    - Crecimiento sostenido en presupuestos y recaudaciones, pero con déficits recurrentes en la mayoría de los años.
    - Años clave como 2017 y 2020 muestran discrepancias significativas debido a eventos económicos y la pandemia de COVID-19.
2. #### Insights por Categorías de Ingresos:
    - Receitas Correntes: Comportamiento estable con superávits en años recientes, especialmente 2021, indicando mejora en la recaudación.
    - Receitas de Capital: Volatilidad notable, con déficits significativos y un superávit excepcional en 2020 vinculado a medidas extraordinarias.
3. ####  Desempeño por Ministerios y Fuentes:
    - Disparidades entre ministerios, con algunos mostrando bajos niveles de recaudación frente a sus presupuestos.
    - Fuentes como "Receitas Patrimoniais" destacan por un desempeño superior a lo previsto, mientras que otras como "Alienação de Bens" necesitan análisis adicional.
4. ####  Retos y Áreas de Mejora:
    - Proyecciones Presupuestarias: Necesidad de estimaciones más realistas basadas en datos históricos y factores externos.
    - Gestión de Ingresos: Monitoreo y mejores prácticas para optimizar la recaudación en ministerios con desempeño bajo.
    - Transparencia: Mejorar sistemas de registro y corregir inconsistencias en datos financieros.

### - **Recomendaciones y Próximos Pasos** 🔄  📈

1. Fortalecimiento de Proyecciones:
    -  Implementar modelos de predicción basados en inteligencia artificial o análisis histórico para reducir las diferencias entre lo previsto y lo recaudado.

2. Optimización de la Recaudación:
    - Identificar ministerios con desempeño bajo y aplicar auditorías o capacitaciones en gestión fiscal para mejorar la eficiencia.

3. Mejoras en la Calidad de Datos:
    - Desarrollar herramientas y procesos que automaticen el registro y clasificación de datos para garantizar consistencia y confiabilidad.

4. Análisis Futuro:
    - Explorar más profundamente las razones detrás de las discrepancias en categorías específicas y evaluar el impacto de políticas gubernamentales sobre las tendencias observadas.
    - Este proyecto establece una base sólida para comprender la dinámica presupuestaria y de recaudación, pero también resalta áreas críticas para el avance hacia una gestión financiera más eficiente y equitativa.

### - **Contribuciones** 🤝 

Las contribuciones son bienvenidas para mejorar este proyecto. Si deseas colaborar, abre un pull request o crea una issue para discutir tus ideas. Se valoran especialmente las contribuciones en las áreas de análisis de datos y visualización.

### - **Autores y Agradecimientos** ✒️ 

**Agustin Salomon**

Repositorios Github
https://github.com/aSalomon96

mi LinkedIn https://www.linkedin.com/in/agustin-salomon/

 