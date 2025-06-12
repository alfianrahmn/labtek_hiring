# Case Study – AI-Powered App with Heterogeneous Data

**Latar Belakang**  
Saya backend engineer dengan 9 tahun pengalaman. Dua tahun terakhir saya fokus pada deploy ML ke production di AWS (ECS/Fargate), membangun FastAPI + async processing, MLOps dengan Jenkins, dan monitoring via CloudWatch.

---

## 1. Desain & Integrasi Data

**1.1 Ingest & Store**  
- **Object Store:** MinIO (S3-compatible)—konsep sama dengan AWS S3; saya pakai MinIO karena sudah familiar dari project sebelumnya.  
- **Structured Data (email):** CSV/JSON di-upload ke `minio://bronze/transactions/`.  
- **Unstructured Data (chat logs, review, sosial media):** disimpan di `minio://bronze/logs/`.  
- **Metadata Catalog:**  
  - Berencana pakai PostgreSQL ringan—sudah pernah saya setup untuk schema registry.  
  - Mempertimbangkan AWS Glue Data Catalog, tapi belum pernah hands-on, referensi saya dapat dari **Google** dan konfirmasi detailnya lewat **ChatGPT**.

**1.2 Bronze → Silver → Gold**  
- **Bronze:** simpan mentah di MinIO.  
- **Silver:** ECS-based Python ETL (Docker + FastAPI or Flask) ekstrak field penting (email, phone, full_name) → Parquet.  
- **Gold:** Python service di ECS menyatukan hasil resolusi menjadi tabel `user_profiles` dalam Delta Lake format di MinIO, jadi setiap write (upsert, delete, merge) bersifat atomik dan terekam history-nya di folder `_delta_log`. 

---

## 2. Entity Resolution & Linking

1. **Primary key:** email apabila tersedia langsung match.  
2. **Sekunder:** bandingkan nomor yang sudah di-normalize (strip non-digit).
3. **Name fuzzy**: akan menggunakan string similarity (Jaro-Winkler) + embedding cosine.  
4. **Clustering**: gabungkan record mirip jadi satu profil.  

> **Catatan Bantuan:**  
> - JSON-parsing & cron syntax & ECS task template & Dockerfile saya cek di Google.  
> - Sliding-window & pseudocode matching & pendekatan fuzzy & clustering saya tanya ke ChatGPT

