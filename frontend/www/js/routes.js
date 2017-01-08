angular.module('app.routes', [])

.config(function($stateProvider, $urlRouterProvider) {

  // Ionic uses AngularUI Router which uses the concept of states
  // Learn more here: https://github.com/angular-ui/ui-router
  // Set up the various states which the app can be in.
  // Each state's controller can be found in controllers.js
  $stateProvider
    
  

      .state('tabsController.schedule', {
    url: '/schedule',
    views: {
      'tab1': {
        templateUrl: 'templates/schedule.html',
        controller: 'scheduleCtrl'
      }
    }
  })

  .state('tabsController.options', {
    url: '/page3',
    views: {
      'tab2': {
        templateUrl: 'templates/options.html',
        controller: 'optionsCtrl'
      }
    }
  })

  .state('tabsController', {
    url: '/page1',
    templateUrl: 'templates/tabsController.html',
    abstract:true
  })

  .state('login', {
    url: '/page5',
    templateUrl: 'templates/login.html',
    controller: 'loginCtrl'
  })

  .state('signup', {
    url: '/signup',
    templateUrl: 'templates/signup.html',
    controller: 'signupCtrl'
  })

  .state('tabsController.addTutorTime', {
    url: '/addtime',
    views: {
      'tab1': {
        templateUrl: 'templates/addTutorTime.html',
        controller: 'addTutorTimeCtrl'
      }
    }
  })

$urlRouterProvider.otherwise('/page5')

  

});