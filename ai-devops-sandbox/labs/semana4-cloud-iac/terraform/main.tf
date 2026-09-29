# Infraestructura de ejemplo para "Orders API" - usa LocalStack, no AWS real.
# Para correr LocalStack: docker run -d -p 4566:4566 localstack/localstack

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region                      = "us-east-1"
  access_key                  = "test"
  secret_key                  = "test"
  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_requesting_account_id  = true

  endpoints {
    s3 = "http://localhost:4566"
  }
}

# Bucket donde se guardan los reportes de órdenes generados por el worker
resource "aws_s3_bucket" "orders_reports" {
  bucket = "orders-reports-bucket"
}

# NOTA: revisa si esta configuración es apropiada para un bucket
# que va a contener reportes de órdenes de clientes.
resource "aws_s3_bucket_acl" "orders_reports_acl" {
  bucket = aws_s3_bucket.orders_reports.id
  acl    = "public-read"
}

resource "aws_s3_bucket_versioning" "orders_reports_versioning" {
  bucket = aws_s3_bucket.orders_reports.id
  versioning_configuration {
    status = "Disabled"
  }
}
