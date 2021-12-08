# Prediccion-meteorlogia-espacial
Este proyecto fue desarrollado como TFG del grado en ingeniería informática impartido por la Universidad de Alcalá, el cual fue propuesto como candidato a matrícula de honor. El objetivo es la predicción de viento solar a través de redes neuronales profundas. <br />

- Es recomendable leer [Documentación.pdf](https://github.com/c-yanguas/Prediccion-meteorologia-espacial/blob/main/Documentaci%C3%B3n.pdf) para comprender los objetivos del proyecto y los pasos realizados.
- Dado que los datos pesan 150 MB no es posible subirlos al respositorio, dejo un enlace para los interesados: [datos sin preprocesar](https://drive.google.com/file/d/1AvvkAYaAC0BMMwAF_6qqtdTqTEbLfcRG/view?usp=sharing) y [datos preprocesados](https://drive.google.com/file/d/1BXSGC21YNVCk8kAn-kHe7qfXJYRtnL-v/view?usp=sharing) <br />

Este proyecto se divide de la siguiente manera:

- Extraccion_datos contiene un script que permite extraer los datos de la página https://omniweb.gsfc.nasa.gov/form/omni_min.html, esta debidamente documentado, por lo que si se quisieran extraer otros datos sería posible modificando la variable 'variables', la cual tiene una ruta html para cada variable. Es importante destacar que este script esta pensado para trabajar con el webdriver de chrome, el cual se puede descargar en: https://chromedriver.chromium.org/.

- Comparativa_metodos_imputacion contiene un notebook en el cual se ofrece una visualización y cunatificación de las comparativas de los diferentes métodos usados para imputar los datos nulos del conjunto de datos inicial.

- Prediccion_Tormenta contiene un notebook que evalua la precisión del mejor modelo obtenido para la predicción de un momento de tormenta.

- Prediccion_tormentas contiene un notebook en el cual se trató de crear modelos únicamente con datos de tormentas.

- Prediccion_general contiene un resumen de los modelos desarrollados, sus métricas asociadas y la predicción de una tormenta en su parte final por el mejor modelo obtenido.
