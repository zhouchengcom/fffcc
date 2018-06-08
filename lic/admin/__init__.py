import flask_admin
from flask_admin.contrib.mongoengine import ModelView

from flask_security import Security, SQLAlchemyUserDatastore, \
    UserMixin, RoleMixin, login_required, current_user

from ..db.user import User, Role
from flask import Flask, url_for, redirect, render_template, request, abort
from ..db.mongomodel import Label


class SnakeModelView(ModelView):

    def is_accessible(self):
        if not current_user.is_active or not current_user.is_authenticated:
            return False

        if current_user.has_role('admin'):
            return True

        return False

    def _handle_view(self, name, **kwargs):
        """
        Override builtin _handle_view in order to redirect users when a view is not accessible.
        """
        if not self.is_accessible():
            if current_user.is_authenticated:
                # permission denied
                abort(403)
            else:
                # login
                abort(400)


def InitAdmin(app):
    admin = flask_admin.Admin(
        app,
        'admin',
        template_mode='bootstrap3',
    )

    # Add model views
    admin.add_view(SnakeModelView(Role))
    admin.add_view(SnakeModelView(User))
    admin.add_view(SnakeModelView(Label))