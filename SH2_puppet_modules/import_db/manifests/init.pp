class import_db {
    require postgresql

    # create postgres user
    exec { "create-postgres-user":
        command => "expect -f /SH2/conf/SH2_puppet_modules/import_db/scripts/createuser.exp",
        require => $osfamily ? {
            "Debian" => Package["postgresql", "expect"],
            "RedHat" => [ Package["postgresql", "expect"], Exec["start-postgres-server"] ],
        }
    }

    # create postgres database
    exec { "create-postgres-db":
        command => "expect -f /SH2/conf/SH2_puppet_modules/import_db/scripts/createdb.exp",
        require => [ Exec["create-postgres-user"], Package["expect"], ],
    }

    # create db directory
    file { '/SH2/db':
        ensure => 'directory',
    }

    # import db dump directly from gz
    exec { "import-db-dump":
         command => "expect -f /SH2/conf/SH2_puppet_modules/import_db/scripts/importdb.exp",
         timeout => 3600,
        require => [ Exec["dl-db-dump"], Package["expect"], ],
    }
}
