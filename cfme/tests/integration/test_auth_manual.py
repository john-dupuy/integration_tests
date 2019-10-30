import pytest

from cfme import test_requirements

pytestmark = [test_requirements.auth]


@pytest.mark.manual
@pytest.mark.tier(1)
def test_appliance_console_ipa():
    """
    Test setting up IPA authentication with invalid host settings

    Polarion:
        assignee: jdupuy
        casecomponent: Auth
        caseimportance: low
        caseposneg: negative
        initialEstimate: 1/6h
    """
    pass


@pytest.mark.manual
@pytest.mark.tier(3)
def test_update_ldap_updates_login():
    """
    Change user/groups attribute in  ldap domain server.
    E.g change user display name
    Verify authentication fails for old display name
    Verify authentication for new display name for the user.
    Verify changing cache_credentials = True
    entry_cache_timeout = 600

    Polarion:
        assignee: jdupuy
        casecomponent: Auth
        caseimportance: low
        initialEstimate: 1/2h
    """
    pass


@pytest.mark.manual
@pytest.mark.tier(3)
def test_saml_verify_user_login():
    """
    Polarion:
        assignee: jdupuy
        casecomponent: Auth
        caseimportance: low
        caseposneg: negative
        initialEstimate: 1/2h
        title: saml: verify user login with and without correct groups added to SAML server.
        testSteps:
            1. Configure CFME for SAML with RHSSO server (cf. appliance.configure_saml)
            2. Try to login with SAML user
        expectedResults:
            1. Login to corporate account should redirect to RHSSO server
            2. User should be logged in with appropriate perms
    """
    pass


@pytest.mark.manual
@pytest.mark.tier(2)
def test_saml_get_user_groups_from_ext_auth_httpd():
    """
    Enable “Get User Groups from External Authentication (httpd)” option.
    Verify “user groups from SAML server are updated correctly and user
    with correct groups can login. (retrieve groups option is not valid in
    case of SAML)

    Polarion:
        assignee: jdupuy
        casecomponent: Auth
        initialEstimate: 1/2h
        title: saml: Verify “Get User Groups from External Authentication (httpd)” option.
    """
    pass


@pytest.mark.manual
@pytest.mark.tier(2)
@pytest.mark.parametrize("mode", ["console", "ui"])
def test_verify_ui_reflects_ext_auth(mode):
    """
    Tests that login screen reflects external auth mode.

    Polarion:
        assignee: jdupuy
        casecomponent: Auth
        caseimportance: low
        initialEstimate: 1/6h
        testSteps:
            1. Select external auth modes
            2. Disable the external auth modes
        expectedResults:
            1. Verify that the login screen UI reflects the auth mode
            2. Login screen goes back to normal
    """
    pass


@pytest.mark.manual
@pytest.mark.tier(2)
@pytest.mark.meta(coverage=[1378213])
def test_ldap_group_lookup_error_message():
    """
    Polarion:
        assignee: jdupuy
        caseimportance: low
        casecomponent: Auth
        caseposneg: negative
        initialEstimate: 1/4h
        title: verify ldap group lookup fails with correct error message
               for invalid user details
        testSteps:
            1. Configure appliance with LDAP server that has no memberOf overlay
            2. Perform user group lookup
        expectedResults:
            1.
            2. Error message saying no groups found for user should be displayed
    Bugzilla:
        1378213
    """
    pass


@pytest.mark.manual
@pytest.mark.tier(2)
def test_verify_user_validation_authentication():
    """
    Polarion:
        assignee: jdupuy
        casecomponent: Auth
        caseimportance: medium
        initialEstimate: 1/4h
        title: verify user validation works fine but authentication fails
               if no group is assigned for user.
        testSteps:
            1. Create user in ldap domain server.
            2. Do not assign any group to the user.
            3. Configure cfme for ldap
            4. Check audit.log and evm.log
            5. Check get users groups in UI
        expectedResults:
            1.
            2.
            3.
            4. logs should say “unable to match user"s group membership to an EVM role” message.
            5. should be disabled
    """
    pass


@pytest.mark.manual
@pytest.mark.tier(2)
def test_verify_role_configuration_for_new_ldap_groups():
    """
    Retrieve ldap user groups, assign roles to the group.
    Login to cfme webui as ldap user and verify user role is working as
    expected.
    NOTE: execute rbac test cases.

    Polarion:
        assignee: jdupuy
        casecomponent: Auth
        caseimportance: medium
        initialEstimate: 1h
        title: verify role configuration work as expected for new ldap groups
    """
    pass


@pytest.mark.manual
@pytest.mark.tier(2)
def test_disable_local_login():
    """
    Polarion:
        assignee: jdupuy
        casecomponent: Auth
        caseimportance: low
        initialEstimate: 1/2h
        title: Verify disable local login option works fine. Verify enable/disable option

        testSteps:
            1. Configure CFME for external auth
            2. Enable "Disable local login"
        expectedResults:
            1.
            2. Admin DB user should no longer be able to login
    """
    pass


@pytest.mark.manual
@pytest.mark.tier(2)
def test_ldap_auth_without_groups():
    """
    verify LDAP authentication works without groups from LDAP
    refer this bz: https://bugzilla.redhat.com/show_bug.cgi?id=1302345
    Steps:
    1.In Configuration->Authentication, set the auth mode to LDAP.
    LDAP Hostname: "cfme-openldap-rhel7.cfme.lab.eng.rdu2.redhat.com"
    LDAP Port: 389
    UserType: Distinguished Name (UID=<user>)
    User Suffix: UID=<user> :  ou=people,ou=prod,dc=psavrocks,dc=com
    2. uncheck the "Get User Groups from LDAP"
    3. In Access Control -> Users, created new user
    "uid=test,ou=people,ou=prod,dc=psavrocks,dc=com" and set Group to
    EvmGroup-administrator
    ("uid=test,ou=people,ou=prod,dc=psavrocks,dc=com" user is already
    created in LDAP Server)
    4. Logout and tried Login with username: test and password: test,
    Login failed.
    Expected results:
    Base DN should always be visible and should be part of the LDAP
    Settings, when it is always needed.

    Polarion:
        assignee: jdupuy
        casecomponent: Auth
        caseimportance: low
        initialEstimate: 1/4h
        title: verify LDAP authentication works without groups from LDAP by
               uncheck the "Get User Groups from LDAP"
    """
    pass


@pytest.mark.manual
@pytest.mark.tier(3)
def test_saml_login_fails_after_password_change():
    """
    Polarion:
        assignee: jdupuy
        casecomponent: Auth
        caseimportance: low
        caseposneg: negative
        initialEstimate: 1/4h
        title: Verify login fails for user in CFME after changing the
               Password in SAML for the user.
        setup:
            1. configure appliance with saml server
        testSteps:
            1. Create user and assign group in saml.
            2. Logout
            3. Change creds in SAML server
        expectedResults:
            1.
            2.
            3. SAML user should not be able to sign in
    """
    pass


@pytest.mark.manual
@pytest.mark.tier(2)
def test_two_factor_auth_with_user_password_and_otp():
    """
    Polarion:
        assignee: jdupuy
        initialEstimate: 1/3h
        casecomponent: Auth
        caseimportance: medium
        title: verify two factor authentication works with user password and otp.
    testSteps:
        1. configure CFME for external auth (IPA, SAML etc..)
        2. configure user for OTP in authentication server.
    expectedResults:
        1.
        2. verify two factor authentication for CFME works with user password
            and otp.
    """
    pass


@pytest.mark.manual
@pytest.mark.tier(2)
def test_auth_mode_new_trusted_forest_table_entry():
    """
    verify the authentication mode is displayed correctly for new trusted
    forest table entry.

    Polarion:
        assignee: jdupuy
        casecomponent: Auth
        caseimportance: low
        initialEstimate: 1/6h
        title: verify the authentication mode is displayed correctly for
               new trusted forest table entry.
    """
    pass


@pytest.mark.manual
@pytest.mark.tier(2)
def test_ldap_invalid_user_login():
    """
    Verifies scenarios associated with the invalid user login(negative
    test case).

    Polarion:
        assignee: jdupuy
        casecomponent: Auth
        caseimportance: low
        caseposneg: negative
        initialEstimate: 1/4h
        testSteps:
            1. login with the invalid user.
            2. configure the ldap with userA in groupA, configure CFME
               for userA and groupA. Login with userA
            3. delete the userA in the ldap. try Login with userA to CFME appliance
        expectedResults:
            1. login should fail for invalid credentials.
            2. login should be successful
            3. login should fail
    """
    pass


@pytest.mark.manual
@pytest.mark.tier(3)
def test_remove_display_name_for_user_in_ldap_and_verify_auth():
    """
    1. Remove display name for user in ldap and verify auth.

    Polarion:
        assignee: jdupuy
        casecomponent: Auth
        caseimportance: low
        caseposneg: negative
        initialEstimate: 1/2h
        title: Remove display name for user in ldap and verify auth.
    """
    pass


@pytest.mark.manual
@pytest.mark.tier(3)
def test_change_search_base():
    """
    Change the search base for user and groups lookup at domain component
    . e.g. change the search level from
    "ou=Groups,ou=prod,dc=qetest,dc=com "
    To "dc=qetest,dc=com"
    Change the ‘ldap_group_search_base’ and ‘ldap_user_search_base’ in
    /etc/sssd/sssd.conf for specific domain.
    Make sure domain_suffix is updated correctly for your ldap domain
    under test.
    Restart sssd service (service sssd restart)
    Verify configuration with dbus commands (refer MOJO)
    Verify user/group retrieval in CFME webui.
    user/group created at any hierarchy level under the tree
    dc=qetest,dc=com is expected to be retrieved.

    Polarion:
        assignee: jdupuy
        casecomponent: Auth
        caseimportance: low
        initialEstimate: 1/2h
        title: Change the search base for user and groups lookup at domain component .
    """
    pass


@pytest.mark.manual
@pytest.mark.tier(3)
def test_change_domain_sequence_sssd_group_retrieval():
    """
    create user1 in test.com
    create group1 in test.com
    assign user1 to group1
    verify for the group retrived for user1
    Only group1 should be displayed in the group list in
    Note:  user should be authenticated with FQDN user1@test.com : group1
    test.com
    user1@qetest.com: qegroup1 qetest.com

    Polarion:
        assignee: jdupuy
        casecomponent: Auth
        caseimportance: low
        initialEstimate: 1/2h
        title: Change the domain sequence in sssd, and verify user groups retrieval.
    """
    pass


@pytest.mark.manual
@pytest.mark.tier(2)
def test_verify_user_groups_can_be_retrieved_from_trusted_forest():
    """
    verify user groups can be retrieved from "trusted forest", when the
    "import roles from home forest" is unchecked.configuration:
    1. Create the user "ldaptest" and group "engineering" in ldap:"cfme-
    qe-ldap", and add "ldaptest" user to "engineering" group.
    2. Create the user "ldaptest" and group "cfme" in ldap:"cfme-qe-ipa"
    and add "ldaptest" user to "cfme" group.
    Steps :
    1. Login as "admin" and navigate to
    configure->configuration->authentication
    2. change the authentication mode to "ldap"
    3. specify the hostname for the "cfme-qe-ipa", as the primary ldap.
    4. in the "Role Settings" check "Get User Groups from LDAP", observe
    that "Trusted Forest Settings" table displayed below. specify "Base
    DN" and "Bind DN"
    5. click on "+" to add "Trusted Forest Settings", specify HostName as
    "cfme-qe-ldap",enter valid Base DN, Bind DN and "Bind Password" click
    add the trusted forest and click "Save"
    6. navigate to "access control"-> "groups"->"add new group", check
    (Look Up LDAP Groups), specify the user "ldaptest", click retrieve.
    Observe that only the groups(cfme) from Primary ldap (cfme-qe-ipa) are
    retrieved. no group(engineering) from "cfme-qe-ldap" is reqtrieved.
    7. manually add the group "engineering", logout and login as
    "ldaptest". Observe that login fails for the user "ldaptest"

    Polarion:
        assignee: jdupuy
        casecomponent: Auth
        caseimportance: low
        initialEstimate: 1/2h
        title: verify user groups can be retrieved from "trusted forest"
    """
    pass


@pytest.mark.manual
@pytest.mark.tier(2)
def test_verify_the_trusted_forest_settings_table_display_in_auth_page():
    """
    verify the trusted forest settings table display in authentication
    page. switch between the authentication modes and check the trusted
    forest settings table does not disappear.

    Polarion:
        assignee: jdupuy
        casecomponent: Auth
        caseimportance: low
        initialEstimate: 1/6h
        title: verify the trusted forest settings table display in authentication page.
    """
    pass


@pytest.mark.manual
@pytest.mark.tier(2)
def test_authentication_user_not_in_ldap_but_in_db():
    """
    User is not able to authenticate if he has account in CFME DB but not
    in LDAP.

    Polarion:
        assignee: jdupuy
        casecomponent: Auth
        caseimportance: medium
        caseposneg: negative
        initialEstimate: 1/4h
    """
    pass


@pytest.mark.manual
@pytest.mark.tier(2)
def test_verify_database_user_login_fails_with_external_auth_configured():
    """
    Login with user registered to cfme internal database.
    Authentication expected to fail, check audit.log and evm.log for
    correct log messages.

    Polarion:
        assignee: jdupuy
        casecomponent: Auth
        caseimportance: medium
        initialEstimate: 1/4h
        title: Verify DataBase user login fails with External auth configured.
    """
    pass


@pytest.mark.manual
@pytest.mark.tier(3)
def test_external_auth_openldap_proxy_to_3_domains():
    """
    verify external authentication with OpenLDAP proxy to 3 different
    domains
    refer the bz: https://bugzilla.redhat.com/show_bug.cgi?id=1306436

    Bugzilla:
        1306436

    Polarion:
        assignee: jdupuy
        casecomponent: Auth
        caseimportance: low
        initialEstimate: 1/2h
        title: verify external authentication with OpenLDAP proxy to 3 different domains
    """
    pass


@pytest.mark.manual
@pytest.mark.tier(2)
def test_appliance_console_ext_auth_options_skip():
    """
    Test skip update of ext_auth options through appliance_console

    Polarion:
        assignee: jdupuy
        casecomponent: Auth
        caseimportance: medium
        initialEstimate: 1/6h
        setup: -ssh to appliance
               -run appliance_console
               -select option "Update External Authentication Options"
               -select each option to enable it
               -select option
               1) Enable/Disable Single Sign-On
               2) Enable/Disable SAML
               3) Enable/Disable Local Login
               -select "Skip updates"
               -check changes have not been made
        startsin: 5.6
        testSteps:
            1. Enable Single Sign-On, SAML, Local Login then select skip updates
            2. Disable Single Sign-On, SAML, Local Login then select skip updates
            3. Enable Single Sign-On then select skip updates
            4. Disable Single Sign-On then select skip updates
            5. Enable SAML then select skip updates
            6. Disable SAML then select skip updates
            7. Enable Local Login then select skip updates
            8. Disable Local Login then select skip updates
        expectedResults:
            1. check changes in ui
            2. check changes in ui
            3. check changes in ui
            4. check changes in ui
            5. check changes in ui
            6. check changes in ui
            7. check changes in ui
            8. check changes in ui
    """
    pass


@pytest.mark.manual
@pytest.mark.tier(2)
def test_multi_domain_configuration_for_external_auth_ldaps():
    """
    Look for the steps/instructions at
    https://mojo.redhat.com/docs/DOC-1085797
    Verify appliance_console is updated with “External Auth: “ correctly.
    Verify appliance_console displays all the domains configured. Now it
    displays only one. There will be BZ.

    Polarion:
        assignee: jdupuy
        casecomponent: Auth
        caseimportance: low
        initialEstimate: 1/2h
        title: verify multi domain configuration for external auth ldaps
    """
    pass


@pytest.mark.manual
@pytest.mark.tier(2)
def test_external_auth_config_for_ldap_appliance_console():
    """
    Run command “appliance_console”
    Select option for “configure external authentication”
    Verify “IPA Client already configured on this Appliance, Un-Configure
    first?” is displayed
    Answer yes to continue with unconfigure process.
    Verify Database user login works fine upon external auth un configured
    and auth mode set to ‘Database’.

    Polarion:
        assignee: jdupuy
        casecomponent: Auth
        caseimportance: medium
        initialEstimate: 1/3h
        title: Verify external auth configuration for ldap can be un
               configured using appliance_console
    """
    pass


@pytest.mark.manual
@pytest.mark.tier(3)
def test_cfme_features_with_ldap():
    """
    verifies the cfme features with authentication mode configured to
    ldap.

    Polarion:
        assignee: jdupuy
        casecomponent: Auth
        caseimportance: medium
        initialEstimate: 1h
        testSteps:
            1. login with ldap user
            2. verify the CFME features after login with ldap user.
        expectedResults:
            1. login should be successful
            2. All the CFME features should work properly with ldap authentication.
    """
    pass


@pytest.mark.manual
@pytest.mark.tier(3)
def test_ldaps_customized_port():
    """
    Configure ldap/ldaps domain server with customized port.
    Configure cfme for customized domain ports. Check mojo page for
    details.
    Verify ldap user/group authentication.

    Polarion:
        assignee: jdupuy
        casecomponent: Auth
        caseimportance: low
        initialEstimate: 1/2h
        title: Configure  ldaps for customized port e.g 10636, 10389 and validate CFME auth
    """
    pass


@pytest.mark.manual
@pytest.mark.tier(3)
def test_saml_multiple_appliances_same_realm():
    """
    Verify configuring more than one appliance to SAML authentication as
    mentioned in Step#1 works fine.

    Polarion:
        assignee: jdupuy
        casecomponent: Auth
        caseimportance: medium
        initialEstimate: 1/2h
        title: saml: Verify multiple appliances can be added to the same REALM.
    """
    pass


@pytest.mark.manual
@pytest.mark.tier(2)
def test_session_timeout():
    """
    As admin change the session timeout in cfme webui.
    Login as ldap user and verify session times out after the specified
    timeout value.

    Polarion:
        assignee: jdupuy
        casecomponent: Auth
        caseimportance: low
        initialEstimate: 1/6h
        title: Verify session timeout works fine for external auth.
    """
    pass
