# 🧱 dbt Data Vault 2.0 — eCommerce Analytics Project

## 🧭 Overview

This project demonstrates how to implement a **Data Vault 2.0 architecture** using `dbt` to model data from multiple sources in the eCommerce and logistics domain.

It integrates data from:
- 🛒 **Shopify** (sales, products, customers)
- 🚚 **3PL Logistics** (shipments, tracking, SLAs)
- 🏢 **Warehouse systems** (inventory, fulfillment)
- 📢 **Marketing platforms** (Meta Ads, Google Ads)
- 💰 **Finance systems** (Oracle Fusion ERP)

The models are deployed and orchestrated using `dbt Cloud` and tested in `Snowflake`.

---

## 🧱 Architecture

- **Staging Layer**: Standardized, cleaned data from each source
- **Hubs**: Business keys (e.g., customer, order, product)
- **Links**: Relationships (e.g., order ↔ shipment)
- **Satellites**: Contextual details (e.g., order status, address, payment)
- **Marts**: Flattened, analytics-ready views

---

## 🧰 Tech Stack

| Component     | Tool/Service             |
|---------------|--------------------------|
| Modeling      | `dbt` (Core + Cloud)     |
| Warehouse     | `Snowflake`              |
| Orchestration | `dbt Cloud` + GitHub CI  |
| Ingestion     | `Airbyte`, `Fivetran`    |
| Versioning    | `GitHub`                 |
| Testing       | `dbt tests`, `snapshots` |

---

## 🚀 How to Run

### 1. Clone the repo
```bash
git clone https://github.com/motiramgh/DBT-ECOMM-DATA-VAULT.git
cd DBT-ECOMM-DATA-VAULT