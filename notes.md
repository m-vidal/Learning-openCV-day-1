Na **OpenCV**, imagens são arrays NumPy, o equivalente a uma matriz
2D/3D no C/C++.
Geralmente possui altura, largura, e cores representadas
pelo int 3.
PS: as cores na **OpenCV**, são armazenadas em BGR e não RGB

O *SSD* (Single Shot Detector), é uma arquitetura de rede neural
que detecta objetos numa única passada pela imagem, ao contrário
da moda antiga que de certa forma era mais manual, ou menos inteligente.
O *SSD* aprendeu a fazer isso internamente.

O *Blob*: quando alimentamos uma imagem a uma rede neural pela **OpenCV**,
ela precisa estar sobre um determinado padrão. Uma especie de conversão
(Ela precisa ser transformada num blob), normalizar valores de pixeis,
redimensionar para o tamanho esperado/aceite pela rede e reorganizar os
canais... Para isso a **OpenCV** tem cv2.dnn.blobFromImage().

Redes neurais possuem os chamados de Pessos (conhecimento adquirido ao longo
do tempo) e Arquitetura (geralmente um ficheiro de texto que descreve quais
caminhos a aprendizagem deve tomar, o que fazer com os dados colhidos, etc).

Man... A opencv-python normal precisa de bibliotecas gráficas do sistema (libGL)
mas ela não existe em Codespaces (pq é um server sem ecrã), por isso precisamos
usar uma versão da OpenCV que foi pensada para este exato contexto: opencv-python-headless

streamlit: pega o código python e converte em uma webpage, existem muitos comandos
simples para cirar elementos na pégina... como:
    .title(""), que coloca uma especie cabeçalho H1 de HTML
    .write(""), que coloca um parágrafo
    .slider("s", 0, 100), gera um slime com o nome do first arg e um range do second to last arg
    .image(frame), display the first arg image an a label (optional second arg)
    .camera_input("Camera"), adivinhe o resto :)
