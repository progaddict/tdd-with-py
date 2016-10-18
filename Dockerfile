FROM python:3-onbuild

EXPOSE 5000

CMD ["gunicorn", "-b 0.0.0.0:5000", "superlists.wsgi:application"]
