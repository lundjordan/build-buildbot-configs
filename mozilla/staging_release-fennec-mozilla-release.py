releaseConfig = {}
releaseConfig['disable_tinderbox_mail'] = True
releaseConfig['base_clobber_url'] = 'http://clobberer-stage.pvt.build.mozilla.org/always_clobber.php'

# Release Notification
releaseConfig['AllRecipients']       = ['<release@mozilla.com>',]
releaseConfig['ImportantRecipients'] = ['<release@mozilla.com>',]
releaseConfig['releaseTemplates']    = 'release_templates'
releaseConfig['messagePrefix']       = '[staging-release] '

# Basic product configuration
#  Names for the product/files
releaseConfig['productName']         = 'fennec'
releaseConfig['appName']             = 'mobile'
releaseConfig['relbranchPrefix']     = 'MOBILE'
#  Current version info
releaseConfig['version']             = '10.0.2'
releaseConfig['appVersion']          = releaseConfig['version']
releaseConfig['milestone']           = releaseConfig['version']
releaseConfig['buildNumber']         = 1
releaseConfig['baseTag']             = 'FENNEC_10_0_2'
#  Next (nightly) version info
releaseConfig['nextAppVersion']      = releaseConfig['version']
releaseConfig['nextMilestone']       = releaseConfig['version']
#  Repository configuration, for tagging
releaseConfig['sourceRepositories']  = {
    'mobile': {
        'name': 'mozilla-release',
        'clonePath': 'releases/mozilla-release',
        'path': 'users/stage-ffxbld/mozilla-release',
        'revision': 'default',
        'relbranch': None,
        'bumpFiles': {
            'mobile/android/confvars.sh': {
                'version': releaseConfig['appVersion'],
                'nextVersion': releaseConfig['nextAppVersion']
            },
            'browser/config/version.txt': {
                'version': releaseConfig['appVersion'],
                'nextVersion': releaseConfig['nextAppVersion']
            },
            'config/milestone.txt': {
                'version': releaseConfig['milestone'],
                'nextVersion': releaseConfig['nextMilestone']
            },
            'js/src/config/milestone.txt': {
                'version': releaseConfig['milestone'],
                'nextVersion': releaseConfig['nextMilestone']
            },
        }
    }
}
#  L10n repositories
releaseConfig['l10nRelbranch']       = None
releaseConfig['l10nRepoClonePath']   = 'releases/l10n/mozilla-release'
releaseConfig['l10nRepoPath']        = 'users/stage-ffxbld'
releaseConfig['l10nRevisionFile']    = 'l10n-changesets_mobile-release.json'
releaseConfig['l10nJsonFile']        = releaseConfig['l10nRevisionFile']
#  Support repositories
releaseConfig['otherReposToTag']     = {
    'users/stage-ffxbld/compare-locales': 'RELEASE_AUTOMATION',
    'users/stage-ffxbld/buildbot': 'production-0.8',
    'users/stage-ffxbld/partner-repacks': 'default',
    'users/stage-ffxbld/mozharness': 'default',
}

# Platform configuration
releaseConfig['enUSPlatforms']        = ('android',)
releaseConfig['notifyPlatforms']      = releaseConfig['enUSPlatforms']
releaseConfig['manuallySignedPlatforms']      = releaseConfig['enUSPlatforms']
releaseConfig['unittestPlatforms']    = ()
releaseConfig['talosTestPlatforms']   = ()
releaseConfig['enableUnittests']      = True

# L10n configuration
releaseConfig['l10nPlatforms']       = ('android',)
releaseConfig['l10nChunks']          = 2
releaseConfig['mergeLocales']        = True
releaseConfig['enableMultiLocale']   = True

# Mercurial account
releaseConfig['hgUsername']          = 'stage-ffxbld'
releaseConfig['hgSshKey']            = '~cltbld/.ssh/ffxbld_dsa'

# Update-specific configuration
releaseConfig['ftpServer']           = 'dev-stage01.srv.releng.scl3.mozilla.com'
releaseConfig['stagingServer']       = 'dev-stage01.srv.releng.scl3.mozilla.com'
releaseConfig['ausServerUrl']        = 'http://dev-stage01.srv.releng.scl3.mozilla.com'
releaseConfig['ausHost']             = 'dev-stage01.srv.releng.scl3.mozilla.com'
releaseConfig['ausUser']             = 'cltbld'
releaseConfig['ausSshKey']           = 'cltbld_dsa'

# Partner repack configuration
releaseConfig['doPartnerRepacks']       = True
releaseConfig['partnersRepoPath']       = 'users/stage-ffxbld/partner-repacks'
releaseConfig['partnerRepackPlatforms'] = ('android',)
releaseConfig['partnerRepackConfig'] = {
    'use_mozharness': True,
    'platforms': {
        'android': {
            'script': 'scripts/mobile_partner_repack.py',
            'config_file': 'partner_repacks/staging_release_mozilla-release_android.py',
         },
    },
}

# mozconfigs
releaseConfig['mozconfigs']          = {
    'android': 'mobile/android/config/mozconfigs/android/release',
}

# Misc configuration
releaseConfig['enable_repo_setup']       = False

# Fennec specific
releaseConfig['usePrettyNames']           = False
releaseConfig['disableBouncerEntries']    = True
releaseConfig['disableStandaloneRepacks'] = True
releaseConfig['disablePermissionCheck']   = True
releaseConfig['disableVirusCheck']        = True
releaseConfig['disablePushToMirrors']     = True

releaseConfig['single_locale_options'] = {
    'android': [
        '--cfg',
        'single_locale/staging_release_mozilla-release_android.py',
        '--user-repo-override', 'users/stage-ffxbld',
        '--tag-override', '%s_RELEASE' % releaseConfig['baseTag'],
    ],
}

releaseConfig['multilocale_config'] = {
    'platforms': {
        'android':
            'multi_locale/staging_release_mozilla-release_android.json',
    },
    'multilocaleOptions': [
        '--tag-override=%s_RELEASE' % releaseConfig['baseTag'],
        '--user-repo-override=users/stage-ffxbld',
        '--only-pull-locale-source',
        '--only-add-locales',
        '--only-package-multi',
    ]
}

# Staging config
releaseConfig['build_tools_repo_path'] = "users/stage-ffxbld/tools"
releaseConfig['skip_release_download'] = True
releaseConfig['enableSigningAtBuildTime'] = False
releaseConfig['enablePartialMarsAtBuildTime'] = False
releaseConfig['autoGenerateChecksums'] = False
