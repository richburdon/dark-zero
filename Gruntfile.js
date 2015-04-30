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

    // TODO(burdon): Patch with local mods (e.g., app.yaml)
    gitPull: {
      all: {
        repos: [
          {
            path: ['src', 'main', 'docker'],
            repo: 'git@github.com:GoogleCloudPlatform/appengine-nginx-hello.git'
          },
          {
            path: ['src', 'main', 'docker'],
            repo: 'git@github.com:kbastani/docker-neo4j.git'
          },
          {
            path: ['src', 'main', 'docker'],
            repo: 'git@github.com:kbastani/spark-neo4j.git'
          }
        ]
      }
    },

    pydeps: {
      options: {
        packages: [
          'flask',                // flask
          'flask_injector.py',    // flask
          'injector.py',          // flask
          'itsdangerous.py',      // flask
          'werkzeug',             // flask
          'yaml',                 // GAE
          'py2neo'
        ]
      },

      all: {}
    },

    // Deploy to App Engine (via OAuth).
    // https://www.npmjs.org/package/grunt-gae
    // > gcloud auth login
    // > gcloud config set project dark-zero
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

  // Nexus task defs.
  grunt.task.loadTasks('../alienlaboratories/core/src/main/grunt/tasks');

  // https://github.com/gruntjs/grunt-contrib-clean
  grunt.loadNpmTasks('grunt-contrib-clean');

  // https://www.npmjs.org/package/grunt-gae
  grunt.loadNpmTasks('grunt-gae');

  // https://www.npmjs.com/package/grunt-gitpull
  grunt.loadNpmTasks('grunt-gitPull');

  // Default
  grunt.registerTask('default', ['gae']);

};
