// Copyright 2014 Alien Laboratories, Inc.

module.exports = function(grunt) {

  grunt.initConfig({

    //
    // npm install (to install/update deps which are added to package.json)
    //
    pkg: grunt.file.readJSON('package.json'),

    // GAE dev_appserver runtime files.
    appserver: 'target/appserver',

    clean: ['target'],

    pydeps: {
      options: {
        packages: [
          'flask',                // flask
          'flask_injector.py',    // flask
          'injector.py',          // flask
          'itsdangerous.py',      // flask
          'werkzeug',             // flask
          'yaml'                  // GAE
        ]
      },

      all: {}
    },

    // Deploy to App Engine (via OAuth).
    // https://www.npmjs.org/package/grunt-gae
    // > gcloud auth login
    // > gcloud config set project nexus-beta
    // > grunt gae:update
    gcloud: {
      options: {
        project: 'dark-zero'
      }
    },

    // App Engine
    gae: {
      options: {
        path: 'src/main/python'
      },
      run: {
        action: 'run',
        options: {
          args: {
            dev_appserver_log_level: 'error',
            storage_path: '<%= appserver %>'
          }
        }
      },
      kill: {
        action: 'kill'
      },
      update: {
        action: 'update'
      },
      rollback: {
        action: 'rollback'
      }
    }

  });

  grunt.task.loadTasks('../alienlaboratories/core/src/main/grunt/tasks');

  // https://github.com/gruntjs/grunt-contrib-clean
  grunt.loadNpmTasks('grunt-contrib-clean');

  // https://www.npmjs.org/package/grunt-gae
  grunt.loadNpmTasks('grunt-gae');

  grunt.registerTask('default', ['gae']);

};
