// Install the Java helper library from twilio.com/docs/java/install

import com.twilio.Twilio;
import com.twilio.base.ResourceSet;
import com.twilio.rest.sync.v1.service.SyncStream;

public class Example {
    // Find your Account Sid and Token at twilio.com/console
    // DANGER! This is insecure. See http://twil.io/secure
    public static final String ACCOUNT_SID = "ACXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX";
    public static final String AUTH_TOKEN = "your_auth_token";

    public static void main(String[] args) {
        Twilio.init(ACCOUNT_SID, AUTH_TOKEN);
        ResourceSet<SyncStream> syncStreams = 
            SyncStream.reader("ISXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
            .limit(20)
            .read();

        for(SyncStream record : syncStreams) {
            System.out.println(record.getSid());
        }
    }
}