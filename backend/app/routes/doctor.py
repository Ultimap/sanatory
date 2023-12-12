from fastapi import APIRouter, Depends, Form, File, UploadFile
from app.models.models import User
from app.depends import get_doctor_serivce, get_spec_serivce, get_current_user_is_admin
from app.services.doctor import DoctorService
from app.services.specialzation import SpecializationService
_doctor = APIRouter(prefix='/api/doctor', tags=['Doctor'])


@_doctor.get('/')
async def get_all_doctor(doctor_service: DoctorService = Depends(get_doctor_serivce),
                         spec_serive: SpecializationService = Depends(get_spec_serivce)):
    doctors = await doctor_service.get_all_doctor()
    for doctor in doctors:
        doctor['spacialization'] = await spec_serive.get_specialization_by_id(doctor['spacialization'])
    return doctors


@_doctor.get('/{doctor_id}')
async def get_doctor_by_id(doctor_id: int,
                           doctor_service: DoctorService = Depends(get_doctor_serivce),
                           spec_serive: SpecializationService = Depends(get_spec_serivce)):
    doctor = await doctor_service.get_doctor_by_id(doctor_id)
    doctor['spacialization'] = await spec_serive.get_specialization_by_id(doctor['spacialization'])
    return doctor


@_doctor.put('/{doctor_id}/add/img')
async def doctor_upload_img(doctor_id: int, img: UploadFile = File(...),
                            doctor_service: DoctorService = Depends(get_doctor_serivce),
                            user: User = Depends(get_current_user_is_admin)):
    await doctor_service.upload_img(doctor_id, img)
    return {'message': 'Success'}

@_doctor.delete('/{doctor_id}/delete')
async def delete_doctor(doctor_id: int,
                        doctor_serivce: DoctorService = Depends(get_doctor_serivce),
                        user: User = Depends(get_current_user_is_admin)):
    await doctor_serivce.delete_doctor(doctor_id)
    return {'meesage': 'Success'}