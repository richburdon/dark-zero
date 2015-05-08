// Copyright 2014 Alien Laboratories, Inc.

module.exports = function(grunt) {

  grunt.initConfig({

    //
    // npm install (to install/update deps which are added to package.json)
    //
    pkg: grunt.file.readJSON('package.json'),

    clean: ['target'],

    pydeps: {
      options: {
        packages: []
      },

      all: {}
    },

    // Python tests.
    // NOTE: Add nose, nose-exclude to requirements.txt
    // https://www.npmjs.org/package/grunt-nose
    // http://nose.readthedocs.org/en/latest/man.html
    // To run tests manually:
    // ./tools/python/bin/python src/main/python/test.py
    nose: {
      options: {
        stop: true,
//      collect_only: true,
        virtualenv: 'tools/python',
        config: 'nose.cfg'
      },
      main: {
        src: [
          'src/main/python'
        ]
      }
    }
  });

  // Nexus task defs.
  grunt.task.loadTasks('../alienlaboratories/core/src/main/grunt/tasks');

  // https://github.com/gruntjs/grunt-contrib-clean
  grunt.loadNpmTasks('grunt-contrib-clean');

  // https://www.npmjs.org/package/grunt-nose
  grunt.loadNpmTasks('grunt-nose');

  // Default
  grunt.registerTask('default', ['gae']);

};
