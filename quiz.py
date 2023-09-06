class Soru:
    def __init__(self, metin, cevap):
        self.metin = metin
        self.cevap = cevap

class Quiz:
    def __init__(self):
        self.sorular = []
        self.skor = 0

    def soru_ekle(self, soru):
        self.sorular.append(soru)

    def sorulari_goster(self):
        for soru in self.sorular:
            print(soru.metin)

    def quizi_baslat(self):
        for soru in self.sorular:
            cevap = input(soru.metin + " Cevabınız: ")
            if cevap.lower() == soru.cevap.lower():
                print("Doğru!\n")
                self.skor += 1
            else:
                print("Yanlış. Doğru cevap: " + soru.cevap + "\n")
        
        print("Quiz sona erdi. Toplam skorunuz:", self.skor)

# Soruları ve cevapları ekleyelim
soru1 = Soru("Python'ın yaratıcısı kimdir?", "Guido van Rossum")
soru2 = Soru("Python hangi tür bir dildir?", "Yüksek Seviyeli Programlama Dili")
soru3 = Soru("Python'da bir değişken nasıl tanımlanır?", "Değişken adı = Değer")

# Quiz'i oluşturalım ve soruları ekleyelim
quiz = Quiz()
quiz.soru_ekle(soru1)
quiz.soru_ekle(soru2)
quiz.soru_ekle(soru3)

# Quiz'i başlat
print("Python Quizine Hoş Geldiniz!")
quiz.quizi_baslat()
