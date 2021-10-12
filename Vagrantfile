Vagrant.configure("2") do |config|

    # Vagrant box to build off of.
    config.vm.box = "ubuntu/bionic64"
    config.disksize.size = '10GB'

    # Forward ports
    config.vm.network :forwarded_port, guest: 22, host: 2225, id: "ssh"
    config.vm.network :forwarded_port, guest: 8000, host: 8080
    config.vm.network :forwarded_port, guest: 80, host: 8081

    # Allocate resources
    config.vm.provider :virtualbox do |vb|
        vb.customize ["modifyvm", :id, "--ioapic", "on"]
        vb.customize ["modifyvm", :id, "--memory", "4096"]
        vb.customize ["modifyvm", :id, "--cpus", "4"]
    end

    # Set up a shared directory
    config.vm.synced_folder "shared", "/SH2/", :owner => "vagrant"

    # copy puppet scripts to VM
    config.vm.provision "file", source: "SH2_puppet_modules", destination: "/SH2/conf/SH2_puppet_modules"
    config.vm.provision "shell", inline: "sudo apt-get update && sudo apt-get install -y puppet"

    # Enable the Puppet provisioner
    config.vm.provision :puppet do |puppet|
        puppet.manifests_path = "manifests"
        puppet.manifest_file = "default.pp"
        puppet.module_path = "SH2_puppet_modules"
    end

end

