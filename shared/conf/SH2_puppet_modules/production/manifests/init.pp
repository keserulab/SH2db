class production {
    # copy production settings to local settings file
    file { "/SH2/sites/SH2/SH2/settings_local.py":
        ensure => present,
        source => "/SH2/sites/SH2/SH2/settings_local_production.py",
        before => Exec["build_blast_db"],
    }
}
