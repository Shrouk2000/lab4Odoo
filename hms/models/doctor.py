from odoo import models, fields


class Doctor(models.Model):
    _name = 'hms.doctor'
    _description = 'Doctor Information'

    first_name = fields.Char(required=True, string="First Name")
    last_name = fields.Char(required=True, string="Last Name")
    image = fields.Binary(string="Image")
    specialty = fields.Char(string="Specialty")
    phone = fields.Char(string="Phone Number")
    email = fields.Char(string="Email")

    # Many2many relationship with patients
    patient_ids = fields.Many2many('hms.patient', string="Patients")
