/*
 * @constructor
 * Init should be called on the object this prototype
 * to make it usable.
 */
var ManageFeeds = function() {}

/*
 * Initializes the ManageFeeds object.
 * Adds click handlers to url elements.
 */
ManageFeeds.prototype.init = function() {
  var self = this;
  $("#add-btn").click(function() {
    self.addFeed(this);
  });
  $("#delete-btn").click(function() {
    self.deleteFeed(this);
  });
}

/*
 *  Posts title and description.
 *  @param {Object} element Clicked DOM object.
 */
ManageFeeds.prototype.addFeed = function(element) {
  var add_url = 'add';
  var self = this;
  var xhr = $.post(add_url, $('#add-frm').serialize())
  xhr.done(function(message) {
    self.updateStatus('Feed Added.');
  });
  xhr.fail(function(e) {
    self.updateStatus('Unable to add feed.');
  });
}

/*
 *  Posts username and password.
 *  @param {Object} element Clicked DOM object.
 */
ManageFeeds.prototype.deleteFeed = function(element) {
  var delete_url = 'delete';
  var self = this;
  var xhr = $.post(delete_url, $('#delete-frm').serialize())
  xhr.done(function(message) {
    self.updateStatus('Feed deleted.');
  });
  xhr.fail(function(e) {
    self.updateStatus('Unable to delete feed.');
  });
}

/*
 * Alerts the status of update.
 *  @param {String} message String containing status message.
 */
ManageFeeds.prototype.updateStatus = function(message) {
  alert(message);
  window.location.reload(true);
}
