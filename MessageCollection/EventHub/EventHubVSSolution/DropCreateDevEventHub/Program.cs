using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using Microsoft.ServiceBus;
using System.Configuration;
using Microsoft.ServiceBus.Messaging;

namespace DropCreateDevEventHub
{
    class Program
    {
        static void Main(string[] args)
        {
            string connectionString = ConfigurationManager.AppSettings["eventHubNamespaceConnectionString"];
            string eventHubName = ConfigurationManager.AppSettings["eventHubName"];
            string eventHubManagePrimaryAndSecondaryKey = ConfigurationManager.AppSettings["eventHubManagePrimaryAndSecondaryKey"];
            string eventHubListenPrimaryAndSecondaryKey = ConfigurationManager.AppSettings["eventHubListenPrimaryAndSecondaryKey"];
            string eventHubSendPrimaryAndSecondaryKey = ConfigurationManager.AppSettings["eventHubSendPrimaryAndSecondaryKey"];

            var manager = NamespaceManager
                .CreateFromConnectionString(connectionString);

            if (manager.EventHubExists(eventHubName))
            {
                Console.WriteLine($"Event hub {eventHubName} already exists, removing it.");
                manager.DeleteEventHub(eventHubName);
            }
            else
            {
                Console.WriteLine($"Event hub {eventHubName} does not already exist.");
            }

            var ehd = new EventHubDescription(eventHubName);
            ehd.PartitionCount = 16;
            ehd.MessageRetentionInDays = 3;

            ehd.Authorization.Add(new SharedAccessAuthorizationRule(
                "ManagePolicy",
                eventHubManagePrimaryAndSecondaryKey,
                eventHubManagePrimaryAndSecondaryKey,
                new AccessRights[] { AccessRights.Send, AccessRights.Listen, AccessRights.Manage }));

            ehd.Authorization.Add(new SharedAccessAuthorizationRule(
                "SendPolicy",
                eventHubSendPrimaryAndSecondaryKey,
                eventHubSendPrimaryAndSecondaryKey,
                new AccessRights[] { AccessRights.Send }));

            ehd.Authorization.Add(new SharedAccessAuthorizationRule(
                "ReceivePolicy",
                eventHubListenPrimaryAndSecondaryKey,
                eventHubListenPrimaryAndSecondaryKey,
                new AccessRights[] { AccessRights.Listen }));

            Console.WriteLine($"Event hub {eventHubName} is being created.");
            manager.CreateEventHub(ehd);

            Console.WriteLine($"Adding consumer groups CG1 and CG2 to event hub {eventHubName}.");
            manager.CreateConsumerGroup(eventHubName, "CG1");
            manager.CreateConsumerGroup(eventHubName, "CG2");

            Console.WriteLine("OK");
            Console.ReadLine();
        }
    }
}
