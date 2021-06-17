import locale
import ghostscript

print("compressing types:")
print("                  1. prepress")
print("                  2. printer")
print("                  3. ebook")
print("                  4. screen")

tipe_compress = int(input("insert compressing type:"))

if tipe_compress == 1:
    jenis = "/prepress"
elif tipe_compress == 2:
    jenis = "/printer"
elif tipe_compress == 3:
    jenis = "/ebook"
elif tipe_compress == 4:
    jenis = "/screen"      


filename = input("insert your file name: ")

args = [
    "BATCH", "-sDEVICE=pdfwrite", "-dCompatibilityLevel=1.4", "-sNAME="+jenis,
    "-sOutputFile=" + filename + "-compressed.pdf", filename+".pdf"]

# arguments have to be bytes, encode them
encoding = locale.getpreferredencoding()
args = [a.encode(encoding) for a in args]
ghostscript.Ghostscript(*args)