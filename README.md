# # **California Housing Prices**
<a href="https://www.kaggle.com/datasets/camnugent/california-housing-prices">Sumber Data housing.csv</a>
## **Ronny Sahat Martua Purba**
### **Daftar Isi**

**I. Business Problem & Data Understanding**

**II. Data Cleaning, Feature selection, & Feature Engineering**

**III. Analytics (Algorithm & Evaluation Metrics)**

**IV. Conclusion and Recommendation**
### **Daftar Isi**

**I. Business Problem & Data Understanding**

**II. Data Cleaning, Feature selection, & Feature Engineering**

**III. Analytics (Algorithm & Evaluation Metrics)**

**IV. Conclusion and Recommendation**

### **I. Business Problem & Data Understanding**

#### **I.1. Context**


Dalam industri real estate, harga properti merupakan salah satu faktor krusial yang menentukan keberhasilan dalam proses jual-beli rumah. Namun, penentuan harga rumah tidaklah mudah karena banyak aspek yang perlu dipertimbangkan, seperti lokasi geografis, kondisi bangunan, kepadatan populasi, serta faktor sosial ekonomi penduduk di sekitar properti tersebut. Penilaian harga secara manual yang dilakukan oleh agen properti atau pemilik rumah kerap kali bersifat subjektif, dan dapat menyebabkan harga yang ditawarkan menjadi tidak sesuai dengan nilai pasar. Akibatnya, rumah bisa sulit terjual karena harga terlalu tinggi, atau sebaliknya pemilik bisa merugi karena harga terlalu rendah.

Di sisi lain, semakin tingginya kebutuhan masyarakat terhadap tempat tinggal, khususnya di negara bagian seperti California yang memiliki dinamika populasi dan ekonomi yang kompleks, menuntut adanya pendekatan berbasis data dalam penentuan harga rumah. Dengan memanfaatkan teknologi dan data historis yang tersedia, *Machine Learning* (ML) dapat digunakan untuk membuat prediksi harga rumah secara lebih objektif dan efisien.

Dataset yang digunakan dalam proyek ini berisi informasi demografis dan geografis dari berbagai wilayah di California, yang masing-masing mewakili satu blok area. Data ini mencakup informasi seperti jumlah kamar, jumlah kamar tidur, jumlah penduduk, pendapatan rata-rata, serta kedekatan lokasi terhadap garis pantai. Data ini memberikan gambaran yang cukup komprehensif untuk dianalisis dan digunakan sebagai dasar dalam membangun model prediksi harga rumah.

Dengan membangun model ML berdasarkan dataset ini, diharapkan dapat membantu stakeholder seperti agen properti, pengembang perumahan, dan calon penjual rumah untuk:

* Menentukan harga rumah yang optimal berdasarkan kondisi lingkungan dan demografis secara otomatis.

* Mempercepat proses valuasi properti dan mengurangi ketergantungan pada intuisi atau estimasi manual.

* Meningkatkan efisiensi dan akurasi dalam transaksi jual-beli rumah.

Secara keseluruhan, proyek ini berfokus pada pengembangan model regresi untuk **memprediksi harga median rumah di California** berdasarkan berbagai fitur yang tersedia, sehingga dapat memberikan insight dan nilai tambah bagi proses bisnis di bidang properti.

#### **I.2. Problem Statement**

Penentuan harga rumah merupakan tantangan yang cukup kompleks karena dipengaruhi oleh banyak faktor yang saling berkaitan, seperti kondisi fisik bangunan, jumlah ruangan, lokasi geografis, hingga faktor sosial ekonomi seperti pendapatan masyarakat sekitar. Proses ini menjadi lebih sulit di wilayah yang dinamis seperti California, di mana permintaan dan nilai properti dapat sangat bervariasi antar wilayah.

**Stakeholder** utama dalam permasalahan ini adalah:

* **Agen properti dan pengembang perumahan** yang bertanggung jawab atas penentuan harga jual properti,

* **Pemilik rumah** yang ingin menjual propertinya dengan harga yang sesuai pasar,

* Dan **calon pembeli** yang ingin mengetahui apakah harga yang ditawarkan sudah sesuai dengan kondisi lingkungan.

Permasalahan yang muncul adalah:

* Tidak adanya alat bantu yang andal untuk **memperkirakan harga rumah secara objektif dan berbasis data**,

* Proses valuasi yang **mengandalkan intuisi atau pengalaman pribadi** seringkali kurang akurat dan tidak konsisten,

* Hal ini dapat menyebabkan **kerugian finansial** bagi penjual maupun pembeli, serta **memperlambat proses transaksi** karena harga tidak sesuai ekspektasi pasar.

**Permasalahan utama (*problem statement*)** yang ingin diselesaikan adalah:

***Bagaimana cara membangun sebuah model prediktif berbasis Machine Learning yang mampu memprediksi harga median rumah di wilayah California secara akurat, dengan mempertimbangkan faktor-faktor lingkungan, demografis, dan geografis yang tersedia dalam dataset?***

Model prediktif ini diharapkan dapat memberikan estimasi harga rumah yang:

* **Akurat** dan mendekati harga pasar sebenarnya,

* **Cepat** dihasilkan tanpa proses manual yang panjang,

* **Konsisten** dalam berbagai wilayah dan kondisi yang berbeda,

* Dan dapat digunakan sebagai **alat bantu pengambilan keputusan bisnis** oleh berbagai pihak yang terlibat dalam industri properti.
