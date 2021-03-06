# ATTENTION:
# If you are editing the non-template version of this file (eg, doesn't end
# with .template), your change WILL get overwritten. If you're adding, removing,
# or changing options as part of release automation changes you should be
# editing the .template instead. This file should only by edited directly if
# you're starting a release without Release Kickoff. You have been warned.
EMAIL_RECIPIENTS = []

releaseConfig = {}
releaseConfig['base_clobber_url'] = 'https://api-pub-build.allizom.org/clobberer/forceclobber'

# Release Notification
releaseConfig['AllRecipients']       = EMAIL_RECIPIENTS
releaseConfig['ImportantRecipients'] = EMAIL_RECIPIENTS
releaseConfig['AVVendorsRecipients'] = EMAIL_RECIPIENTS
releaseConfig['releaseTemplates']    = 'release_templates'
releaseConfig['messagePrefix']       = '[staging-release] '

# Basic product configuration
#  Names for the product/files
releaseConfig['productName']         = 'thunderbird'
releaseConfig['stage_product']       = 'thunderbird'
releaseConfig['appName']             = 'mail'
releaseConfig['relbranchPrefix']     = 'THUNDERBIRD'
releaseConfig['mozilla_srcdir']      = 'mozilla'
#  Current version info
releaseConfig['version']             = '33.0b1'
releaseConfig['appVersion']          = '33.0'
releaseConfig['milestone']           = releaseConfig['appVersion']
releaseConfig['buildNumber']         = 1
releaseConfig['baseTag']             = 'THUNDERBIRD_33_0b1'
releaseConfig['partialUpdates']      = {

    '32.0b1': {
        'appVersion': '32.0',
        'buildNumber': 1,
        'baseTag': 'THUNDERBIRD_32_0b1',
    },

}
#  Next (nightly) version info
releaseConfig['nextAppVersion']      = releaseConfig['appVersion']
releaseConfig['nextVersion']         = releaseConfig['version']
releaseConfig['nextMilestone']       = releaseConfig['milestone']
#  Repository configuration, for tagging
releaseConfig['sourceRepositories']  = {
    'comm': {
        'name': 'comm-beta',
        'path': 'users/stage-ffxbld/comm-beta',
        'revision': 'default',
        'relbranch': None,
        'bumpFiles': {
            'mail/config/version.txt': {
                'version': releaseConfig['appVersion'],
                'nextVersion': releaseConfig['nextAppVersion']
            },
            'mail/config/version_display.txt': {
                'version': releaseConfig['version'],
                'nextVersion': releaseConfig['nextVersion']
            },

        }
    },
    'mozilla': {
        'name': 'mozilla-beta',
        'path': 'users/stage-ffxbld/mozilla-beta',
        'revision': 'default',
        'relbranch': None,
        'bumpFiles': {
            'config/milestone.txt': {
                'version': releaseConfig['milestone'],
                'nextVersion': releaseConfig['nextMilestone']
            },
        },
    }
}
#  L10n repositories
releaseConfig['l10nRelbranch']       = None
releaseConfig['l10nRepoPath']        = 'users/stage-ffxbld'
releaseConfig['l10nRevisionFile']    = 'l10n-changesets_thunderbird-beta'
#  Support repositories
releaseConfig['otherReposToTag']     = {
    'users/stage-ffxbld/compare-locales': 'RELEASE_AUTOMATION',
    'users/stage-ffxbld/buildbot': 'production-0.8',
    'users/stage-ffxbld/mozharness': 'production',
}

# Platform configuration
releaseConfig['enUSPlatforms']       = ('linux', 'linux64', 'win32', 'macosx64')
releaseConfig['notifyPlatforms']     = releaseConfig['enUSPlatforms']
releaseConfig['talosTestPlatforms']  = ()

# Unittests
releaseConfig['unittestPlatforms']   = ()
releaseConfig['enableUnittests']     = True

# L10n configuration
releaseConfig['l10nPlatforms']       = releaseConfig['enUSPlatforms']
releaseConfig['shippedLocalesPath']  = 'mail/locales/shipped-locales'
releaseConfig['l10nChunks']          = 6
releaseConfig['mergeLocales']        = True
releaseConfig['l10nUsePymake']       = True

# Mercurial account
releaseConfig['hgUsername']          = 'stage-ffxbld'
releaseConfig['hgSshKey']            = '/home/mock_mozilla/.ssh/ffxbld_rsa'

# Update-specific configuration
releaseConfig['ftpServer']           = 'ftp.stage.mozaws.net'
releaseConfig['stagingServer']       = 'upload.tbirdbld.productdelivery.stage.mozaws.net'
releaseConfig['previousReleasesStagingServer'] = 'archive.mozilla.org'
releaseConfig['S3Credentials']       = '/builds/release-s3.credentials'
releaseConfig['S3Bucket']            = 'net-mozaws-stage-delivery-archive'
releaseConfig['bouncerServer']       = 'download.mozilla.org'
releaseConfig['ausServerUrl']        = 'https://aus4-dev.allizom.org'
releaseConfig['releaseNotesUrl']     = 'http://live.mozillamessaging.com/thunderbird/releasenotes?locale=%locale%&platform=%platform%&version=%version%'
releaseConfig['testOlderPartials']   = False
releaseConfig['promptWaitTime']      = None
releaseConfig['mozconfigs']          = {
    'linux': 'mail/config/mozconfigs/linux32/release',
    'linux64': 'mail/config/mozconfigs/linux64/release',
    'macosx64': 'mail/config/mozconfigs/macosx64/release',
    'win32': 'mail/config/mozconfigs/win32/release',
}
releaseConfig['source_mozconfig']      = 'mail/config/mozconfigs/linux64/source'
releaseConfig['releaseChannel']        = 'beta'
releaseConfig['updateChannels'] = {
    "beta": {
        "versionRegex": r"^.*$",
        "ruleId": 33,
        "patcherConfig": "mozBeta-thunderbird-branch-patcher2.cfg",
        "localTestChannel": "beta-localtest",
        "cdnTestChannel": "beta-cdntest",
        "verifyConfigs": {
            "linux":  "mozBeta-thunderbird-linux.cfg",
            "linux64":  "mozBeta-thunderbird-linux64.cfg",
            "macosx64": "mozBeta-thunderbird-mac64.cfg",
            "win32":  "mozBeta-thunderbird-win32.cfg",
        },
        "testChannels": {
            "beta-cdntest": {
                "ruleId": 43,
            },
            "beta-localtest": {
                "ruleId": 21,
            },
        }
    }
}

# Partner repack configuration
releaseConfig['doPartnerRepacks']    = False

# Tuxedo/Bouncer configuration
releaseConfig['tuxedoServerUrl']     = 'https://admin-bouncer-releng.stage.mozaws.net/api'
releaseConfig['bouncer_submitter_config'] = 'releases/bouncer_thunderbird.py'
releaseConfig['bouncer_aliases']     = {
    'Thunderbird-%(version)s': 'thunderbird-beta-latest',
}

# Misc configuration
releaseConfig['build_tools_repo_path'] = "users/stage-ffxbld/tools"
releaseConfig['enableAutomaticPushToMirrors'] = True
releaseConfig['use_mock'] = True
releaseConfig['mock_platforms'] = ('linux','linux64')
releaseConfig['extra_signing_env'] = {'TOOLTOOL_DIR': '%(basedir)s/comm-beta'}
