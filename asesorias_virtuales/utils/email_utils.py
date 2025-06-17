from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings
from django.utils.html import strip_tags
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
from django.contrib.auth import get_user_model
from apps.usuarios.models import Asesor, Aprendiz, Coordinador
import logging

logger = logging.getLogger(__name__)
User = get_user_model()

def send_welcome_email(user):
    """Send welcome email to new users"""
    try:
        subject = '¡Bienvenido a Asesorías Virtuales!'
        html_content = render_to_string('emails/welcome.html', {
            'user': user,
            'role': user.get_role_display() if hasattr(user, 'get_role_display') else user.role
        })
        text_content = strip_tags(html_content)
        
        msg = EmailMultiAlternatives(
            subject,
            text_content,
            settings.DEFAULT_FROM_EMAIL,
            [user.email]
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return True
    except Exception as e:
        logger.error(f"Error sending welcome email: {str(e)}")
        return False

def send_group_assignment_email(asesor, grupo):
    """Send email to advisor when assigned to a group"""
    try:
        subject = f'Asignación de Grupo: {grupo.nombre}'
        html_content = render_to_string('emails/group_assignment.html', {
            'asesor': asesor,
            'grupo': grupo,
            'aprendices': grupo.aprendices.all()
        })
        text_content = strip_tags(html_content)
        
        msg = EmailMultiAlternatives(
            subject,
            text_content,
            settings.DEFAULT_FROM_EMAIL,
            [asesor.usuario.email]
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return True
    except Exception as e:
        logger.error(f"Error sending group assignment email: {str(e)}")
        return False

def send_pqrs_notification(pqrs):
    """Send notification for new PQRS"""
    try:
        subject = f'Nueva PQRS: {pqrs.asunto}'
        html_content = render_to_string('emails/pqrs_notification.html', {
            'pqrs': pqrs,
            'user': pqrs.usuario
        })
        text_content = strip_tags(html_content)
        
        # Send to coordinators
        coordinadores = Coordinador.objects.all()
        coordinator_emails = [coordinador.usuario.email for coordinador in coordinadores]
        
        msg = EmailMultiAlternatives(
            subject,
            text_content,
            settings.DEFAULT_FROM_EMAIL,
            coordinator_emails
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return True
    except Exception as e:
        logger.error(f"Error sending PQRS notification: {str(e)}")
        return False

def send_meeting_link_email(reunion):
    """Send meeting link to participants"""
    try:
        subject = f'Link de Reunión: {reunion.titulo}'
        html_content = render_to_string('emails/meeting_link.html', {
            'reunion': reunion,
            'link': reunion.link_reunion
        })
        text_content = strip_tags(html_content)
        
        # Get all participant emails
        participant_emails = [participante.usuario.email for participante in reunion.participantes.all()]
        
        msg = EmailMultiAlternatives(
            subject,
            text_content,
            settings.DEFAULT_FROM_EMAIL,
            participant_emails
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return True
    except Exception as e:
        logger.error(f"Error sending meeting link: {str(e)}")
        return False

def send_group_max_reached_notification(grupo):
    """Send notification when group reaches maximum capacity"""
    try:
        subject = f'Grupo {grupo.nombre} ha alcanzado su capacidad máxima'
        html_content = render_to_string('emails/group_max_reached.html', {
            'grupo': grupo,
            'asesor': grupo.asesor
        })
        text_content = strip_tags(html_content)
        
        # Send to coordinators
        coordinadores = Coordinador.objects.all()
        coordinator_emails = [coordinador.usuario.email for coordinador in coordinadores]
        
        msg = EmailMultiAlternatives(
            subject,
            text_content,
            settings.DEFAULT_FROM_EMAIL,
            coordinator_emails
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return True
    except Exception as e:
        logger.error(f"Error sending group max notification: {str(e)}")
        return False

def send_test_notification(prueba):
    """Send notification for new test"""
    try:
        subject = f'Nueva Prueba: {prueba.titulo}'
        html_content = render_to_string('emails/test_notification.html', {
            'prueba': prueba,
            'grupo': prueba.grupo
        })
        text_content = strip_tags(html_content)
        
        # Get all student emails in the group
        student_emails = [aprendiz.usuario.email for aprendiz in prueba.grupo.aprendices.all()]
        
        msg = EmailMultiAlternatives(
            subject,
            text_content,
            settings.DEFAULT_FROM_EMAIL,
            student_emails
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return True
    except Exception as e:
        logger.error(f"Error sending test notification: {str(e)}")
        return False

def send_account_blocked_email(user):
    """Send email to user when their account is blocked"""
    try:
        subject = 'Cuenta bloqueada - S&S Asesorías Virtuales'
        html_content = render_to_string('emails/account_blocked.html', {'user': user})
        text_content = strip_tags(html_content)
        msg = EmailMultiAlternatives(
            subject,
            text_content,
            settings.DEFAULT_FROM_EMAIL,
            [user.email]
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return True
    except Exception as e:
        logger.error(f"Error sending account blocked email: {str(e)}")
        return False

def send_account_unlock_request(user):
    """Send email to coordinators when a user requests account unlock"""
    try:
        subject = f'Solicitud de desbloqueo de cuenta: {user.get_full_name()}'
        html_content = render_to_string('emails/account_unlock_request.html', {'user': user})
        text_content = strip_tags(html_content)
        coordinadores = Coordinador.objects.all()
        coordinator_emails = [coordinador.usuario.email for coordinador in coordinadores]
        msg = EmailMultiAlternatives(
            subject,
            text_content,
            settings.DEFAULT_FROM_EMAIL,
            coordinator_emails
        )
        msg.attach_alternative(html_content, "text/html")
        msg.send()
        return True
    except Exception as e:
        logger.error(f"Error sending account unlock request: {str(e)}")
        return False 