Vagrant.configure("2") do |config|
  config.vm.box = "ubuntu/bionic64"
  
  # Forward port 5001 from guest to host
  config.vm.network :forwarded_port, guest: 5001, host: 5001
end
