
import inspect

from django.http import HttpResponseNotFound


def dispatch(request_type, action):
  """Decorator to transform the view class methods to be treated 
     Django views.
  """
  def dispatcher(handler_to_call):
    def WrappedFunc(*args, **kwargs):
      return handler_to_call(*args, **kwargs)
    setattr(WrappedFunc, 'request_type', request_type)
    setattr(WrappedFunc, 'action', action)
    return WrappedFunc
  return dispatcher


class BaseView(object):

  def __call__(self, request, *args, **kwargs):
    """Dispatch the url to relevant handler.

    Args:
      request: django.http.HttpRequest representing the request being handled.
      *args: args for method.
      **kwargs: keyword args for method.

    Returns:
      Returns response from the called handler.
      Returns HttpResponseNotFound when AttributeError or TypeError.
    """

    if not kwargs.get('action'):
      kwargs['action'] = 'default'

    callee = None;

    def is_view(member):
      return inspect.ismethod(member) and request.method.upper() == getattr(
         member, 'request_type', False) and kwargs['action'] == getattr(
         member, 'action', False)

    members = inspect.getmembers(self, predicate=is_view)

    for member_name, _ in members:
      callee = getattr(self, member_name)

    del kwargs['action']
    if not callee:
      return HttpResponseNotFound()
    else:
      return callee(request, **kwargs)

