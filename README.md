# Prediccion-meteorlogia-espacial
TFG: Predicción de viento solar a través de redes neuronales profundas. <br />

- Para obtener los datos sin preprocesar y preprocesados por favor visitar: https://drive.google.com/drive/folders/13lgVcPWyBtjmtBnZRfiY6f80u6qLgj9p?usp=sharing <br />

- Es recomendable leer Documentación.pdf para comprender los objetivos del proyecto y los pasos realizados.


<br />

Este proyecto se divide de la siguiente manera:

- Extraccion_datos contiene un script que permite extraer los datos de la pagina https://omniweb.gsfc.nasa.gov/form/omni_min.html esta debidamente documentado por lo que si se quisieran extraer otros datos sería posible modificando la variable 'variables' la cual tiene una ruta html para cada variable. Es importante destacar que este script esta pensado para trabajar con el webdriver de chrome, el cual se puede descargar en: https://chromedriver.chromium.org/

- Comparativa_metodos_imputacion contiene un notebook en el cual se ofrece una visualización y cunatificación de las comparativas de los diferentes métodos usados para interpolar los datos nulos del conjunto de datos inicial.

- Prediccion_Tormenta contiene un notebook que evalua la precisión del mejor modelo obtenido para la predicción de un momento de tormenta.

- Prediccion_tormentas contiene un notebook en el cual se trató de crear modelos únicamente con datos de tormentas.

-Prediccion_general contiene un resumen de los modelos desarrollados, sus métricas asociadas y la predicción de una tormenta en su parte final por el mejor modelo obtenido.
