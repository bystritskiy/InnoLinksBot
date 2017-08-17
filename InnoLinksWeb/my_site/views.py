# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, render_to_response
from django.contrib import auth
from django.template.context_processors import csrf
import gspread
from oauth2client.service_account import ServiceAccountCredentials
from django.contrib.auth import logout


def login(request):
    args = {}
    args.update(csrf(request))
    if request.POST:

        username = request.POST.get('login', '')
        password = request.POST.get('password', '')
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('main/')
        else:
            args['login_error'] = "Пользователь не найден!!!"
            return render_to_response('authorization.html', args)

    else:
        return render_to_response('authorization.html', args)


def form_main(request):
    user = auth.get_user(request)

    if user.is_authenticated:

        row = user.first_name
        scope = ['https://spreadsheets.google.com/feeds']
        creds = ServiceAccountCredentials.from_json_keyfile_name('secret.json', scope)
        client = gspread.authorize(creds)
        sheet = client.open('Карточки организаций InnoHelpBot').sheet1
        if request.POST:
            sheet.update_cell(row, 1, request.POST.get('Name', ''))
            sheet.update_cell(row, 4, request.POST.get('description', ''))
            sheet.update_cell(row, 5, request.POST.get('address', ''))
            sheet.update_cell(row, 6, request.POST.get('telephone', ''))
            sheet.update_cell(row, 7, request.POST.get('mode_of_operation', ''))
            sheet.update_cell(row, 8, request.POST.get('links', ''))
            name = sheet.cell(row, 1).value
            category = sheet.cell(row, 2).value
            subcategory = sheet.cell(row, 3).value
            description = sheet.cell(row, 4).value
            address = sheet.cell(row, 5).value
            telephone = sheet.cell(row, 6).value
            mode_of_operation = sheet.cell(row, 7).value
            links = sheet.cell(row, 8).value
            args = True
            return render(request, 'main.html', {'name': name, 'category': category, 'subcategory': subcategory,
                                                       'description': description, 'address': address,
                                                       'telephone': telephone, 'mode_of_operation': mode_of_operation,
                                                       'links': links, 'args':args})
        else:

            name = sheet.cell(row, 1).value
            category = sheet.cell(row, 2).value
            subcategory = sheet.cell(row, 3).value
            description = sheet.cell(row, 4).value
            address = sheet.cell(row, 5).value
            telephone = sheet.cell(row, 6).value
            mode_of_operation = sheet.cell(row, 7).value
            links = sheet.cell(row, 8).value
            return render(request, 'main.html', {'name': name, 'category': category, 'subcategory': subcategory,
                                                 'description': description, 'address': address,
                                                 'telephone': telephone, 'mode_of_operation': mode_of_operation,
                                                 'links': links})
    else:

        return redirect('/')


def logout_site(request):
    logout(request)
    return redirect('/')
