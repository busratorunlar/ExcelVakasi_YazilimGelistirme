import pandas as pd # pandas küthüpanesini çalıştırıyoruz ve 'pd' kısayoluna tanımlıyoruz.
df= pd.read_excel("ExcelVaka YG.xlsx") # bilgisayarımızdaki "Excel Vaka YG.xlsx" dosyasını okumasını sağlıyoruz.
df[7]= df.iloc [:,4] + df.iloc[:,5] + df.iloc[:,6] #5., 6. ve 7. sütundaki değerlerin toplamını 8. sütuna yazdırıyoruz.
#!! index numaraları pythonda 0dan başladığı için her sütunu -1 fazlasını yazarak kullanıyoruz.!!
def kontrol_et(değer): #değerlerin 100den büyük olup olmadığını kontrol edecek bir fonksiyon tanımlıyoruz.
 if değer > 100: #'değer' 100den büyükse 'False'değerini döndürüyoruz.
  return False 
 else:# Diğer tüm drumlarda (100e eşit ve 100den küçük  olma) True değerini döndürür.
  return True 
df[8] = df[7].apply(kontrol_et)# kontrol_et fonksiyonunu 8. sütuna uyguluyoruz ve sonucunu 9. sütunun tamamına yazdırıyoruz.
true_df = df[df.iloc[:, 7] == True] # 9. sütundaki değerlere bakıp true olan değerlerde tüm satırı seçmesini sağlıyoruz.
with pd.ExcelWriter("Excel Vaka YG.xlsx", engine='openpyxl', mode ='a') as writer:# Excel dosyasını wazmak icin Excel writeri kullanıyoruz ve yazmak istediğimiz dosyanın tam adını kullanıyoruz.
 #mode appened ile dosyayı ekleme modunda çalıştırıyoruz, openpyxl eklentisin ile yeni bir sheet oluşturuyoruz
 true_df.to_excel(writer, sheet_name='Puanlaması_Doğru_Öğrenciler', index=False) # seçtiğimiz true yazılı satırları Puanlaması_Doğru_Öğrenciler sheetine yazdırıyoruz,
 #index=False ile yeni sheete index munaralarının yazılmamasını sağlıyoruz ve dosyayı kapatıyoruz

