import typing as t
import logging


def check_role(
    user,
    with_role: str = None,
    with_roles: t.List[str] = None,
):
    """
    ユーザのロールを確認する
    :param user: ユーザの辞書
    :param with_role: 一致するロール
    :param with_roles: 一致するロールのリスト
    :return: ロールが一致したらTrue, 一致しなければFalse

    example:
    @app.get("/admin")
    @check_login
    def admin_index(request: Request, session_id=Cookie(default=None)):
        user = session.get(session_id).get("user")
        if not check_role(user, with_role="admin"):
            return RedirectResponse("/")
        return templates.TemplateResponse("admin.html", {"request": request, "user": user})
    """
    if with_role is None and with_roles is None:
        raise TypeError("with_role or with_roles is required")
    if with_role is not None and with_roles is not None:
        raise TypeError("with_role and with_roles cannot be used together")

    role = user.get("role")
    if not role:
        logging.warning(f"Role is {role}, is seems a None-like value")

    if with_role is not None:
        return role == with_role

    if with_roles is not None:
        return role in with_roles
