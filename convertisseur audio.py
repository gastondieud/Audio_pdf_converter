import fitz
import io
import pyaudio
import wave
import gtts 

# Spécifiez le nom du fichier PDF d'entrée
pdf_file = "Henoch.pdf"

# Ouvrir le fichier PDF en mode lecture binaire
with open(pdf_file, "rb") as f:
    # Utiliser PyMuPDF pour lire le contenu du PDF
    pdf = fitz.open(f)
    content = ""
    for i in range(pdf.page_count):
        content += pdf.load_page(i).get_text("text") + "\n"

# Convertir le contenu du PDF en audio
tts = gtts.gTTS(content)

# Créer un objet fichier en mémoire
fp = io.BytesIO()
tts.write_to_fp(fp)

# Initialiser PyAudio
p = pyaudio.PyAudio()

# Ouvrir le fichier audio en lecture
stream = p.open(format=p.get_format_from_width(2), channels=1, rate=44100, output=True)

# Lire les données audio à partir du fichier en mémoire et les jouer en temps réel
stream.write(fp.getvalue())

# Fermer la lecture audio
stream.stop_stream()
stream.close()
p.terminate()
