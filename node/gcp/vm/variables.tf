# ================== Project specific configuration
variable "prefix" {
  type    = string
  default = "eu1-bitglob"
}

variable "project" {
  type    = string
  default = "bitcoin-global-playground"
}

variable "region" {
  type    = string
  default = "europe-west1"
}

variable "region_zone" {
  type    = string
  default = "europe-west1-b"
}

# ================== Instance specific configuration
variable "type" {
  type    = string
  default = "g1-small"
}

variable "image" {
  type    = string
  default = "eu.gcr.io/bitcoin-global-playground/bitglobal-node:bootstrap"
}

variable "mount_path" {
  type    = string
  default = "/bitcoin-global"
}

variable "command" {
  type    = list(string)
  default = ["bitglobd"]
}

variable "args" {
  type    = list(string)
  default = [
    "-bootstrap",
    "-testnet"
  ]
}

variable "tags" {
  type    = list(string)
  default = ["bitcoin-global", "btg-node"]
}

variable "expose_ports" {
  type    = list(string)
  default = ["8222", "8332", "8333", "18222", "18332", "18333"]
}
