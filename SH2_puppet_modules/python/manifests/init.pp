
# install packages inside the virtualenv with pip
define puppet::install::pip ($pip_package = $title) {
    exec { "install-$pip_package":
        command => "/env/bin/pip3 install $pip_package",
        timeout => 1800,
        require => [Package["postgresql", "postgresql-contrib"], Exec["create-virtualenv"]]
    }
}

class python {

    $packages = $operatingsystem ? {
        "Ubuntu" => [
                "python3.7",
                "python3.7-dev",
                "python3.7-venv",
                "python3-pip",
                # for python2, will be removed
                "python-biopython",
                "python-openbabel",
                "python-rdkit",
                "python-yaml",
                "libpq-dev",
        ],
        "CentOS" => [
                "python37",
                "python37-devel",
                # for python2, will be removed
                "python-biopython",
                "python-openbabel",
                #"python-rdkit",
                "PyYAML",
        ],
    }

    # install packages
    package { $packages:
        ensure => present,
        require => Exec["update-package-repo"]
    }

    # create a python3 symlink, because the names of the executable differ between OSes
    file { "/usr/local/bin/python3":
        ensure => "link",
        target => "/usr/bin/python3.7",
        require => $operatingsystem ? {
            "CentOS" => Package["python37"],
            "Ubuntu" => Package["python3.7"],
        }
    }

    # install pip
    # exec { "install-pip":
    #    cwd => "/tmp",
    #    command => $operatingsystem ? {
    #        "CentOS" => "wget https://bootstrap.pypa.io/get-pip.py;python3 get-pip.py",
    #        "Ubuntu" => "apt install -y python3-pip",
    #    },
    #}


    # create virtualenv
    exec { "create-virtualenv":
        command => "python3.7 -m venv /env",
    }

    $pip_packages = ["ipython", "django", "django-debug-toolbar", "psycopg2-binary", "biopython", "xlrd", "numpy", "PyYAML",
        "djangorestframework", "django-rest-swagger", "XlsxWriter", "sphinx", "openpyxl", "xmltodict", "cython", "pandas",
	    "django-polymorphic", "mmtf-python", "scipy", "sklearn", "freesasa", "lxml", "reportlab", "svglib", "matplotlib"]
    puppet::install::pip { $pip_packages: }


}
