# Generated by Django 4.2.6 on 2023-11-13 20:10

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('main', '0190_alter_inventorysource_source_and_more'),
        ('dab_rbac', '__first__'),
    ]

    operations = [
        # Add custom permissions for all special actions, like update, use, adhoc, and so on
        migrations.AlterModelOptions(
            name='credential',
            options={'ordering': ('name',), 'permissions': [('use_credential', 'Can use credential in a job or related resource')]},
        ),
        migrations.AlterModelOptions(
            name='instancegroup',
            options={'permissions': [('use_instancegroup', 'Can use instance group in a preference list of a resource')]},
        ),
        migrations.AlterModelOptions(
            name='inventory',
            options={
                'ordering': ('name',),
                'permissions': [
                    ('use_inventory', 'Can use inventory in a job template'),
                    ('adhoc_inventory', 'Can run ad hoc commands'),
                    ('update_inventory', 'Can update inventory sources in inventory'),
                ],
                'verbose_name_plural': 'inventories',
            },
        ),
        migrations.AlterModelOptions(
            name='jobtemplate',
            options={'ordering': ('name',), 'permissions': [('execute_jobtemplate', 'Can run this job template')]},
        ),
        migrations.AlterModelOptions(
            name='project',
            options={
                'ordering': ('id',),
                'permissions': [('update_project', 'Can run a project update'), ('use_project', 'Can use project in a job template')],
            },
        ),
        migrations.AlterModelOptions(
            name='workflowjobtemplate',
            options={
                'permissions': [
                    ('execute_workflowjobtemplate', 'Can run this workflow job template'),
                    ('approve_workflowjobtemplate', 'Can approve steps in this workflow job template'),
                ]
            },
        ),
        migrations.AlterModelOptions(
            name='organization',
            options={
                'default_permissions': ('change', 'delete', 'view'),
                'ordering': ('name',),
                'permissions': [
                    ('member_organization', 'Basic participation permissions for organization'),
                    ('audit_organization', 'Audit everything inside the organization'),
                ],
            },
        ),
        migrations.AlterModelOptions(
            name='team',
            options={'ordering': ('organization__name', 'name'), 'permissions': [('member_team', 'Inherit all roles assigned to this team')]},
        ),
        # Remove add default permission for a few models
        migrations.AlterModelOptions(
            name='jobtemplate',
            options={
                'default_permissions': ('change', 'delete', 'view'),
                'ordering': ('name',),
                'permissions': [('execute_jobtemplate', 'Can run this job template')],
            },
        ),
        migrations.AlterModelOptions(
            name='instancegroup',
            options={
                'default_permissions': ('change', 'delete', 'view'),
                'permissions': [('use_instancegroup', 'Can use instance group in a preference list of a resource')],
            },
        ),
    ]
