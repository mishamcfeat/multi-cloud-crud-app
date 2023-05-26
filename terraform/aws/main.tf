provider "<provider-name>" {
  credentials = file("<path-to-credentials-file>")
  project     = "<project-id>"
  region      = "<region>"
}

resource "<provider-specific-resource-for-instance>" "<resource-name>" {
  name         = "<instance-name>"
  machine_type = "<machine-type>"
  zone         = "<zone>"

  boot_disk {
    initialize_params {
      image = "<image-name>"
    }
  }

  network_interface {
    network = "<network-name>"
  }

  metadata_startup_script = "sudo docker run -d -p 5000:5000 <docker-image-name>"

  service_account {
    scopes = ["<scopes>"]
  }
}
